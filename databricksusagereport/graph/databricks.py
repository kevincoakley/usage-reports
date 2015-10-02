#!/usr/bin/env python

import re
from datetime import datetime
from databricksusagereport.graph.graph import Graph


class DataBricksGraph(Graph):

    def __init__(self):
        Graph.__init__(self)
        self.title = "Cluster Worker Usage"
        self.type = "bar"

    def create(self, usage_list=None, history_list=None):
        if history_list is not None:
            updated_list = []

            for history in history_list:
                history["date"] = datetime.strptime(history["date"][:19], '%Y-%m-%d %H:%M:%S')
                updated_list.append(history)

            updated_list.extend(usage_list)
            usage_list = updated_list

        usage_list_transformed = dict()

        for usage in usage_list:
            # We only want letters and numbers in the name
            name = re.sub("[^A-Za-z0-9]", "_", usage["name"])

            if name not in usage_list_transformed.keys():
                usage_list_transformed[name] = {"x": [usage["date"]],
                                                "y": [usage["numWorkers"]]}
            else:
                usage_list_transformed[name]["x"].append(usage["date"])
                usage_list_transformed[name]["y"].append(usage["numWorkers"])

        return Graph.populate_template(self, usage_list_transformed)
