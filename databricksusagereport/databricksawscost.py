#!/usr/bin/env python

import os
import logging
from datetime import datetime
from pkg_resources import resource_string
import databricksusagereport.arguments
from databricksusagereport.usage.aws import AwsUsage
from databricksusagereport.storage.storage import Storage
from databricksusagereport.graph.aws import AWSGraph


def main():
    args = databricksusagereport.arguments.parse_arguments()

    if args["debug"] is True:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(level=log_level,
                        format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        handlers=[logging.StreamHandler()])

    logging.info('STARTED: databricks-aws-cost')

    aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", None)
    aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY", None)

    if aws_access_key_id is None or aws_secret_access_key is None:
        logging.info("Missing aws_access_key_id and aws_secret_access_key")
        return False
    else:
        logging.debug("aws_access_key_id: %s", aws_access_key_id)
        logging.debug("aws_secret_access_key: %s", aws_secret_access_key[:3])

    if args["aws_storage"] and aws_access_key_id is not None and aws_secret_access_key is not None:
        logging.info("Using AWS storage")
        so = Storage(aws_access_key_id=aws_access_key_id,
                     aws_secret_access_key=aws_secret_access_key)
    else:
        logging.info("No storage method found, check environment variables")
        return False

    storage = so.get_storage()

    if storage is None:
        return False

    aws_usage = AwsUsage(aws_access_key_id, aws_secret_access_key)
    logging.info("Downloading and parsing the latest AWS detailed billing report")
    aws_clusters_cost = aws_usage.get()
    logging.debug("aws_cost: %s", aws_clusters_cost)

    aws_graph = AWSGraph()
    aws_cost_graphs = aws_graph.create(usage_list=aws_clusters_cost)

    for key, value in aws_cost_graphs.iteritems():
        # Construct the upload_directory based on the cluster name and month
        upload_directory = "clusters/cost/%s/%s/%s" % (key,
                                                       datetime.now().strftime("%Y"),
                                                       datetime.now().strftime("%m"))
        if args["aws_storage"]:
            logging.info("Uploading indexes to AWS: %s", upload_directory)
            storage.upload_index(upload_directory)

        logging.info("Upload directory: %s", upload_directory)

        # Upload index.html
        index_html = resource_string("databricksusagereport", "html/index.html")
        storage.upload("%s/index.html" % upload_directory, index_html)

        # Upload graph-data.js
        storage.upload("%s/graph-data.js" % upload_directory, value)

    logging.info('FINISHED: databricks-aws-cost')
