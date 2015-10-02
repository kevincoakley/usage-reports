#!/usr/bin/env python

import os
import json
import logging
import requests
from datetime import datetime
from pkg_resources import resource_string
from databricksusagereport.databricks.usage import DatabricksUsage
from databricksusagereport.github import GitHub
from databricksusagereport.graph.databricks import DatabricksGraph


def transform_history_dict(history_dict):
    history_list = []

    for history_item in history_dict:
        history_item["date"] = str(history_item["date"])[:19]
        history_list.append(history_item)

    logging.debug("transform_history_dict: %s", history_list)
    return history_list


def main():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(name)s %(levelname)s %(message)s',
                        handlers=[logging.StreamHandler()])

    logging.info('STARTED: databricks-workers')

    databricks_username = os.environ.get("DATABRICKS_USERNAME", None)
    databricks_password = os.environ.get("DATABRICKS_PASSWORD", None)
    github_token = os.environ.get("GITHUB_TOKEN", None)

    logging.debug("databricks_username: %s", databricks_username)
    logging.debug("databricks_password: %s", databricks_password[:3])
    logging.debug("github_token: %s", github_token[:3])

    if databricks_username is None or databricks_password is None or github_token is None:
        logging.info("Missing databricks_username, databricks_password or github_token")
        return False

    # Construct the upload_directory based on the year and week of the year
    upload_directory = "clusters/usage/%s/%s" % (datetime.now().strftime("%Y"),
                                                 datetime.now().strftime("%W"))
    logging.info("GitHub Upload directory: %s", upload_directory)

    databricks_usage = DatabricksUsage(databricks_username, databricks_password)
    try:
        logging.info("Connecting to Databricks API")
        databricks_workers = databricks_usage.get()
        logging.debug("databricks_workers: %s", databricks_workers)
    except requests.exceptions.ConnectionError:
        logging.info("Unable to connect to Databricks API")
        return False

    github = GitHub(github_token)

    # Download the databricks workers history from GitHub
    downloaded_history = github.download(upload_directory + "/history.json")
    logging.debug("downloaded_history:  %s", downloaded_history)

    if downloaded_history is None:
        # Upload index.html
        index_html = resource_string("databricksusagereport", "html/index.html")
        github.upload("%s/index.html" % upload_directory, index_html)

        # Upload graph-data.js
        databricks_graph = DatabricksGraph()
        github.upload("%s/graph-data.js" % upload_directory,
                      databricks_graph.create(usage_list=databricks_workers))

        # Upload history.json
        history_list = transform_history_dict(databricks_workers)
        history_json = json.dumps(history_list, ensure_ascii=True, sort_keys=True,
                                  indent=4, separators=(',', ': '))
        github.upload("%s/history.json" % upload_directory, history_json)
    else:
        history_dict = json.loads(downloaded_history)

        # Upload graph-data.js
        databricks_graph = DatabricksGraph()
        github.upload("%s/graph-data.js" % upload_directory,
                      databricks_graph.create(usage_list=databricks_workers,
                                              history_list=history_dict))

        # Upload history.json
        history_dict.extend(databricks_workers)
        logging.debug("history_dict: %s", history_dict)

        history_list = transform_history_dict(history_dict)
        history_json = json.dumps(history_list, ensure_ascii=True, sort_keys=True,
                                  indent=4, separators=(',', ': '))
        github.upload("%s/history.json" % upload_directory, history_json)

    logging.info('FINISHED: databricks-workers')
