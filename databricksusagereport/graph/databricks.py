#!/usr/bin/env python

from datetime import datetime
from databricksusagereport.graph.graph import Graph


class DataBricksGraph(Graph):

    def __init__(self):
        Graph.__init__(self)
        self.title = "Cluster Worker Usage"
        self.mode = "lines+markers"

    def create(self, *args):
        if len(args) == 1 and isinstance(args[0], list):
            usage_list = args[0]
        elif len(args) == 2 and isinstance(args[0], list) and isinstance(args[1], list):
            # If a history_list is included, extend the history_list with the usage_list
            # and set that combination as the usage_list
            usage_list = []

            for history in args[1]:
                history["date"] = datetime.strptime(history["date"], '%Y-%m-%d %H:%M:%S')
                usage_list.append(history)

            usage_list.extend(args[0])
        else:
            raise TypeError("usage_list is required, history_list is optional")

        usage_list_transformed = dict()

        for usage in usage_list:
            if usage["name"] not in usage_list_transformed.keys():
                usage_list_transformed[usage["name"]] = {"x": [usage["date"]],
                                                         "y": [usage["NumWorkers"]]}
            else:
                usage_list_transformed[usage["name"]]["x"].append(usage["date"])
                usage_list_transformed[usage["name"]]["y"].append(usage["NumWorkers"])

        return Graph.populate_template(self, usage_list_transformed)
