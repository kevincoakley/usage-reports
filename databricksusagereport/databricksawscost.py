#!/usr/bin/env python

import re
import logging
import argparse
from datetime import datetime
from pkg_resources import resource_string
from databricksusagereport.usage.aws import AwsUsage
from databricksusagereport.storage.aws import StorageAWS
from databricksusagereport.graph.aws import AWSGraph


def main(save_bucket=None, report_bucket=None, path=None):
    parser = argparse.ArgumentParser()

    parser.add_argument("-b",
                        metavar="save_bucket",
                        dest="save_bucket",
                        help="AWS bucket where the billing report graphs should be saved.",
                        required=True)

    parser.add_argument("-r",
                        metavar="report_bucket",
                        dest="report_bucket",
                        help="AWS bucket where the billing report is stored.",
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

    logging.debug("save_bucket: %s, report_bucket: %s, path: %s, args[\"save_bucket\"]: %s, "
                  "args[\"report_bucket\"]: %s, args[\"path\"]: %s", save_bucket, report_bucket,
                  path, args["save_bucket"], args["report_bucket"], args["path"])

    if save_bucket is None:
        save_bucket = args["save_bucket"]

    if report_bucket is None:
        report_bucket = args["report_bucket"]

    if path is None:
        path = args["path"]

    logging.info("Using AWS storage")
    storage = StorageAWS()

    aws_usage = AwsUsage()
    logging.info("Downloading and parsing the latest AWS detailed billing report")

    logging.info("Report Bucket: %s, Path: %s", report_bucket, path)
    if path is None:
        aws_clusters_cost = aws_usage.get_current(report_bucket)
    else:
        aws_clusters_cost = aws_usage.get(report_bucket, path)

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

        logging.info("Uploading indexes to AWS: %s / %s", save_bucket, upload_directory)
        storage.upload_index(save_bucket, upload_directory)

        logging.info("Upload directory: %s / %s", save_bucket, upload_directory)

        # Upload index.html
        index_html = resource_string("databricksusagereport", "html/index.html")
        storage.upload(save_bucket, "%s/index.html" % upload_directory, index_html)

        # Upload graph-data.js
        storage.upload(save_bucket, "%s/graph-data.js" % upload_directory, value)

    logging.info('FINISHED: databricks-aws-cost')
