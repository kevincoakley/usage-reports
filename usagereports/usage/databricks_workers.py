#!/usr/bin/env python

import logging
import requests
import datetime


class DatabricksWorkersUsage:

    def __init__(self, username, password):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.username = username
        self.password = password

    def get(self):
        self.logger.info("Started get")

        r = requests.get('https://dbc-f6057a15-2f8d.cloud.databricks.com:34563/'
                         'api/1.1/clusters/list', auth=(self.username, self.password))

        json_output = r.json()

        self.logger.info("jsonoutput: %s", json_output)

        databricks_usage_list = []
        for server in json_output:
            d = {'name': server['name'], 'numWorkers': server['numWorkers'],
                 'date': datetime.datetime.now()}
            databricks_usage_list.append(d)

        self.logger.debug("return_var: %s", databricks_usage_list)

        return databricks_usage_list
