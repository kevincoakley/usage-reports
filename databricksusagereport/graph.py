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
        usage_list_transformed = dict()

        for usage in usage_list:
            if usage["name"] not in usage_list_transformed.keys():
                usage_list_transformed[usage["name"]] = {"x": [usage["date"]],
                                                         "y": [usage["NumWorkers"]]}
            else:
                usage_list_transformed[usage["name"]]["x"].append(usage["date"])
                usage_list_transformed[usage["name"]]["y"].append(usage["NumWorkers"])

        graph_data = ""

        for key, value in usage_list_transformed.iteritems():
            # Sort X an Y values by X to achieve chronological order
            y = [y for (x, y) in sorted(zip(value["x"], value["y"]))]
            x = sorted(value["x"])

            graph_data += Graph.graph_data_template % (key,
                                                       "'%s'" % "', '".join(map(str, x)),
                                                       ', '.join(map(str, y)),
                                                       key,
                                                       "lines+markers")

        graph_data_list = ', '.join(map(str, usage_list_transformed.keys()))
        title = "Cluster Worker Usage"

        filled_template = Graph.databricks_graph_data_template % (graph_data,
                                                                  graph_data_list,
                                                                  title)
        return filled_template
