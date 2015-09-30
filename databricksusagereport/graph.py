#!/usr/bin/env python

from pkg_resources import resource_string


class Graph:

    databricks_graph_data_template = resource_string("databricksusagereport",
                                                     "templates/databricks-graph-data.js")
    graph_data_template = resource_string("databricksusagereport",
                                          "templates/graph-data.js")

    def __init__(self):
        pass

    @staticmethod
    def create(usage_list):

        graph_data = ""

        for usage in usage_list:
            graph_data += Graph.graph_data_template % (usage["name"], "'%s'" % usage["date"], usage["NumWorkers"], usage["name"], "lines+markers")

        graph_data_list = "team1, team2, team3"
        title = "Cluster Worker Usage"

        filled_template = Graph.databricks_graph_data_template % (graph_data,
                                                                  graph_data_list,
                                                                  title)
        return filled_template
