#!/usr/bin/env python

import logging
import requests
import datetime


class DatabricksUsage:

    def __init__(self, username, password):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.username = username
        self.password = password

    def get(self):
        self.logger.info("Started get")

        r = requests.get('https://dbc-f6057a15-2f8d.cloud.databricks.com:34563/'
                         'api/1.1/clusters/list', auth=(self.username, self.password))

        jsonoutput = r.json()

        self.logger.info("jsonoutput: %s", jsonoutput)

        return_var = []
        for server in jsonoutput:
            d = {'name': server['name'], 'numWorkers': server['numWorkers'],
                 'date': datetime.datetime.now()}
            return_var.append(d)

        self.logger.debug("return_var: %s", return_var)

        return return_var
