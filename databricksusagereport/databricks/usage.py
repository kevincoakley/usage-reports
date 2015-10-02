#!/usr/bin/env python

import requests
import datetime


class DatabricksUsage:

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def get(self):
        r = requests.get('https://dbc-f6057a15-2f8d.cloud.databricks.com:34563/'
                         'api/1.1/clusters/list', auth=('username', 'password'))
        print r.status_code
        print r.headers['content-type']
        print r.encoding
        print r.text
        print r.json()

        jsonoutput = r.json()
        return_var = []
        for server in jsonoutput:
            d = {'name': server['name'], 'numWorkers': server['numWorkers'],
                 'date': datetime.datetime.now()}
            return_var.append(d)

        return return_var
