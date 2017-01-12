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

    def get(self):
        self.logger.info("Started Databricks Workers get")

        api_url = "https://%s/api/2.0/clusters/list" % self.server

        self.logger.info("requesting: %s", api_url)

        r = requests.get(api_url, auth=(self.username, self.password))

        json_output = r.json()

        self.logger.info("jsonoutput: %s", json_output)

        databricks_usage_list = []
        for server in json_output["clusters"]:
            d = {'name': server['cluster_name'], 'numWorkers': server['num_workers'],
                 'date': datetime.datetime.now()}
            databricks_usage_list.append(d)

        self.logger.debug("return_var: %s", databricks_usage_list)

        return databricks_usage_list
