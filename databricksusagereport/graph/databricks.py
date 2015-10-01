#!/usr/bin/env python

from databricksusagereport.graph.graph import Graph


class DataBricksGraph(Graph):

    def __init__(self):
        Graph.__init__(self)
        self.title = "Cluster Worker Usage"
        self.mode = "lines+markers"

    def create(self, usage_list):
        usage_list_transformed = dict()

        for usage in usage_list:
            if usage["name"] not in usage_list_transformed.keys():
                usage_list_transformed[usage["name"]] = {"x": [usage["date"]],
                                                         "y": [usage["NumWorkers"]]}
            else:
                usage_list_transformed[usage["name"]]["x"].append(usage["date"])
                usage_list_transformed[usage["name"]]["y"].append(usage["NumWorkers"])

        return Graph.populate_template(self, usage_list_transformed)
