#!/usr/bin/env python

import logging
from pkg_resources import resource_string


class Graph:

    databricks_graph_data_template = resource_string("databricksusagereport",
                                                     "templates/databricks-graph-data.js")
    graph_data_template = resource_string("databricksusagereport",
                                          "templates/graph-data.js")

    def __init__(self):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.title = None
        self.type = None
        self.xaxis = None
        self.yaxis = None

    def populate_template(self, usage_list):
        self.logger.info("Started populate_template")
        graph_data = ""

        self.logger.debug("title: %s", self.title)
        self.logger.debug("type: %s", self.type)
        self.logger.debug("usage_list: %s", usage_list)

        for key, value in usage_list.iteritems():
            # Sort X an Y values by X to achieve chronological order
            y = [y for (x, y) in sorted(zip(value["x"], value["y"]))]
            x = sorted(value["x"])

            # Only return YYYY-MM-DD HH of the datetime
            def substring(string_input):
                return str(string_input)[:13]

            x = map(substring, x)

            graph_data += Graph.graph_data_template % (key,
                                                       "'%s'" % "', '".join(map(str, x)),
                                                       ', '.join(map(str, y)),
                                                       key,
                                                       self.type)

        graph_data_list = ', '.join(map(str, usage_list.keys()))

        self.logger.debug("graph_data: %s", graph_data)
        self.logger.debug("graph_data_list: %s", graph_data_list)

        filled_template = Graph.databricks_graph_data_template % (graph_data,
                                                                  graph_data_list,
                                                                  self.title,
                                                                  self.xaxis,
                                                                  self.yaxis)
        self.logger.debug("filled_template: %s", filled_template)

        return filled_template
