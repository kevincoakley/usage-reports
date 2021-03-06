#!/usr/bin/env python

import logging
import requests
import datetime


class DatabricksWorkersUsage:

    def __init__(self, username, password, server):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.username = username
        self.password = password
        self.server = server
        self.raw_json = None

    def get(self):
        self.logger.info("Started Databricks Workers get")

        api_url = "https://%s/api/2.0/clusters/list" % self.server

        self.logger.info("requesting: %s", api_url)

        r = requests.get(api_url, auth=(self.username, self.password))

        self.raw_json = r.json()

        self.logger.info("raw_json: %s", self.raw_json)

        running_clusters = 0
        terminated_clusters = 0

        databricks_usage_list = []
        for server in self.raw_json["clusters"]:
            if server["state"] == "TERMINATED":
                terminated_clusters += 1
            else:
                running_clusters += 1
                d = {'name': server['cluster_name'], 'numWorkers': server['num_workers'],
                     'date': datetime.datetime.now()}
                databricks_usage_list.append(d)

        self.logger.info("Running clusters: %s ; Terminated clusters: %s",
                         running_clusters, terminated_clusters)
        self.logger.debug("return_var: %s", databricks_usage_list)

        return databricks_usage_list
