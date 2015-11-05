#!/usr/bin/env python

import os
import re
import logging
import argparse
from datetime import datetime
from pkg_resources import resource_string
from databricksusagereport.usage.aws import AwsUsage
from databricksusagereport.storage.aws import StorageAWS
from databricksusagereport.graph.aws import AWSGraph


def main(bucket=None, path=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("-b",
                        metavar="bucket",
                        dest="bucket",
                        help="AWS bucket where the billing reports are saved.",
                        required=True)

    parser.add_argument("-p",
                        metavar="path",
                        dest="path",
                        help="Path to the billing report. The billing report for the current month "
                             "will be used if no path is specified.",
                        default=None,
                        required=False)

    parser.add_argument('--debug',
                        dest="debug",
                        action='store_true')

    args = vars(parser.parse_args())

    if args["debug"] is True:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(level=log_level,
                        format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        handlers=[logging.StreamHandler()])

    logging.info('STARTED: databricks-aws-cost')

    logging.debug("bucket: %s, path: %s, args[\"bucket\"]: %s, args[\"path\"]: %s", bucket, path,
                  args["bucket"], args["path"])

    if bucket is None:
        bucket = args["bucket"]

    if path is None:
        path = args["path"]

    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", None)
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY", None)

    if aws_access_key_id is None or aws_secret_access_key is None:
        logging.info("Missing aws_access_key_id and aws_secret_access_key")
        return False
    else:
        logging.debug("aws_access_key_id: %s", aws_access_key_id)
        logging.debug("aws_secret_access_key: %s", aws_secret_access_key[:3])

    logging.info("Using AWS storage")

    storage = StorageAWS(aws_access_key_id, aws_secret_access_key)

    aws_usage = AwsUsage(aws_access_key_id, aws_secret_access_key)
    logging.info("Downloading and parsing the latest AWS detailed billing report")

    logging.info("Bucket: %s, Path: %s", bucket, path)
    if path is None:
        aws_clusters_cost = aws_usage.get_current(bucket)
    else:
        aws_clusters_cost = aws_usage.get(bucket, path)

    logging.debug("aws_cost: %s", aws_clusters_cost)

    aws_graph = AWSGraph()
    aws_cost_graphs = aws_graph.create(usage_list=aws_clusters_cost)

    for key, value in aws_cost_graphs.iteritems():
        # Construct the upload_directory based on the cluster name and month
        if path is None:
            year = datetime.now().strftime("%Y")
            month = datetime.now().strftime("%m")
            logging.debug("year: %s, month: %s (system time)", year, month)
        else:
            year = re.search('-(\d{4})-', path).group(1)
            month = re.search('-(\d{2})\.', path).group(1)
            logging.debug("year: %s, month: %s (path)", year, month)

        upload_directory = "clusters/cost/%s/%s/%s" % (key, year, month)

        logging.info("Uploading indexes to AWS: %s", upload_directory)
        storage.upload_index(upload_directory)

        logging.info("Upload directory: %s", upload_directory)

        # Upload index.html
        index_html = resource_string("databricksusagereport", "html/index.html")
        storage.upload("%s/index.html" % upload_directory, index_html)

        # Upload graph-data.js
        storage.upload("%s/graph-data.js" % upload_directory, value)

    logging.info('FINISHED: databricks-aws-cost')
