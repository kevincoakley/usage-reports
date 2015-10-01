#!/usr/bin/env python

from databricksusagereport.graph.graph import Graph


class DataBricksGraph(Graph):

    def __init__(self):
        Graph.__init__(self)

    @staticmethod
    def create(usage_list):
        usage_list_transformed = dict()

        for usage in usage_list:
            if usage["name"] not in usage_list_transformed.keys():
                usage_list_transformed[usage["name"]] = {"x": [usage["date"]],
                                                         "y": [usage["NumWorkers"]]}
            else:
                usage_list_transformed[usage["name"]]["x"].append(usage["date"])
                usage_list_transformed[usage["name"]]["y"].append(usage["NumWorkers"])

        return Graph.populate_template(usage_list_transformed,
                                       "Cluster Worker Usage",
                                       "lines+markers")
