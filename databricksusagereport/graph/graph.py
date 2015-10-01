#!/usr/bin/env python

from pkg_resources import resource_string


class Graph:

    databricks_graph_data_template = resource_string("databricksusagereport",
                                                     "templates/databricks-graph-data.js")
    graph_data_template = resource_string("databricksusagereport",
                                          "templates/graph-data.js")

    def __init__(self):
        self.title = None
        self.mode = None

    def populate_template(self, usage_list):
        graph_data = ""

        for key, value in usage_list.iteritems():
            # Sort X an Y values by X to achieve chronological order
            y = [y for (x, y) in sorted(zip(value["x"], value["y"]))]
            x = sorted(value["x"])

            graph_data += Graph.graph_data_template % (key,
                                                       "'%s'" % "', '".join(map(str, x)),
                                                       ', '.join(map(str, y)),
                                                       key,
                                                       self.mode)

        graph_data_list = ', '.join(map(str, usage_list.keys()))

        filled_template = Graph.databricks_graph_data_template % (graph_data,
                                                                  graph_data_list,
                                                                  self.title)
        return filled_template
