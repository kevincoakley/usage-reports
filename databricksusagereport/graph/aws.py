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
        self.xaxis = "Date"
        self.yaxis = "Cost"

    def create(self, usage_list=None):
        self.logger.info("Started create")

        self.logger.debug("usage_list: %s", usage_list)

        usage_list_transformed = dict()

        for usage in usage_list:
            # We only want letters and numbers in the name
            name = re.sub("[^A-Za-z0-9]", "_", usage["name"])

            # Cluster is not in usage_list_transformed
            if name not in usage_list_transformed.keys():
                usage_list_transformed[name] = {"x": [usage["date"].date()],
                                                "y": ["{0:.02f}".format(usage["cost"])]}

            # Cluster and date are in usage_list_transformed
            elif name in usage_list_transformed.keys() and \
                    usage["date"].date() in usage_list_transformed[name]["x"]:
                date_index = usage_list_transformed[name]['x'].index(usage["date"].date())
                date_cost = float(usage_list_transformed[name]["y"][date_index]) + usage["cost"]
                usage_list_transformed[name]["y"][date_index] = "{0:.02f}".format(date_cost)

            # Cluster is in usage_list_transformed but date is not
            else:
                usage_list_transformed[name]["x"].append(usage["date"].date())
                usage_list_transformed[name]["y"].append("{0:.02f}".format(usage["cost"]))

        self.logger.debug("usage_list_transformed: %s", usage_list_transformed)

        clusters = dict()

        for key, value in usage_list_transformed.iteritems():
            clusters[key] = Graph.populate_template(self, {key: value})

        return clusters
