#!/usr/bin/env python

import re
import logging
from databricksusagereport.graph.graph import Graph


class AWSGraph(Graph):

    def __init__(self):
        Graph.__init__(self)
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.title = "AWS Cluster Cost"
        self.type = "bar"
        self.xaxis = "Date (UTC)"
        self.yaxis = "Cost"

    def create(self, usage_list=None):
        self.logger.info("Started create")

        self.logger.debug("usage_list: %s", usage_list)

        usage_list_transformed = dict()

        for key, value in usage_list.iteritems():
            # We only want letters and numbers in the name
            name = re.sub("[^A-Za-z0-9]", "_", key)

            x_axis = []
            y_axis = []

            count = 0

            # Sum hourly cost to create a daily total
            for date in value["date"]:
                if date.date() in x_axis:
                    x_axis_date_index = x_axis.index(date.date())
                    date_cost = float(y_axis[x_axis_date_index]) + float(value["cost"][count])
                    y_axis[x_axis_date_index] = "{0:.02f}".format(date_cost)
                else:
                    x_axis.append(date.date())
                    y_axis.append("{0:.02f}".format(value["cost"][count]))

                count += 1

            usage_list_transformed[name] = {"x": x_axis,
                                            "y": y_axis}

        self.logger.debug("usage_list_transformed: %s", usage_list_transformed)

        clusters = dict()

        for key, value in usage_list_transformed.iteritems():
            clusters[key] = Graph.populate_template(self, {key: value})

        return clusters
