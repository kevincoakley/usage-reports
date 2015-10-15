import unittest
import datetime
from databricksusagereport.graph.aws import AWSGraph


class AWSGraphTestCase(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        self.aws_usage_single_file = ["tests/graph/aws_usage_single.js"]
        self.aws_usage_single = {"team1":
                                 {"date": [datetime.datetime(2015, 10, 1, 1, 0, 0),
                                           datetime.datetime(2015, 10, 1, 2, 0, 0),
                                           datetime.datetime(2015, 10, 1, 3, 0, 0),
                                           datetime.datetime(2015, 10, 2, 1, 0, 0),
                                           datetime.datetime(2015, 10, 3, 1, 0, 0),
                                           datetime.datetime(2015, 10, 1, 4, 0, 0),
                                           datetime.datetime(2015, 10, 3, 1, 0, 0)],
                                  "cost": [1.00, 1.25, .75, .50, .50, .33, 1.25]}
                                 }

        self.aws_usage_multiple_file = ["tests/graph/aws_usage_multiple_1.js",
                                        "tests/graph/aws_usage_multiple_2.js",
                                        "tests/graph/aws_usage_multiple_3.js"]

        self.aws_usage_multiple = {"team1":
                                   {"date": [datetime.datetime(2015, 10, 1, 1, 0, 0),
                                             datetime.datetime(2015, 10, 1, 2, 0, 0),
                                             datetime.datetime(2015, 10, 2, 1, 0, 0),
                                             datetime.datetime(2015, 10, 3, 1, 0, 0),
                                             datetime.datetime(2015, 10, 3, 3, 0, 0)],
                                    "cost": [3.00, 0.33, 0.50, 1.50, 0.25]},
                                   "team2":
                                       {"date": [datetime.datetime(2015, 10, 1, 4, 0, 0),
                                                 datetime.datetime(2015, 10, 1, 5, 0, 0),
                                                 datetime.datetime(2015, 10, 2, 1, 0, 0),
                                                 datetime.datetime(2015, 10, 3, 1, 0, 0),
                                                 datetime.datetime(2015, 10, 3, 1, 0, 0)],
                                        "cost": [2.50, 2.50, 0.50, 1.50, 0.75]},
                                   "team3":
                                       {"date": [datetime.datetime(2015, 10, 3, 3, 0, 0),
                                                 datetime.datetime(2015, 10, 3, 1, 0, 0),
                                                 datetime.datetime(2015, 10, 1, 1, 0, 0),
                                                 datetime.datetime(2015, 10, 1, 2, 0, 0),
                                                 datetime.datetime(2015, 10, 2, 5, 0, 0)],
                                        "cost": [2.00, 2.25, 0.12, 0.13, 1.50]},
                                   }

    def test_aws_graph_single(self):
        aws_graph = AWSGraph()

        teams = ["team1"]

        valid_output = dict()

        for team in teams:
            with open(self.aws_usage_multiple_file[teams.index(team)], "r") as f:
                valid_output[team] = f.read()

        self.assertEqual(aws_graph.create(usage_list=self.aws_usage_single), valid_output)

    def test_aws_graph_multiple(self):
        aws_graph = AWSGraph()

        teams = ["team1", "team2", "team3"]

        valid_output = dict()

        for team in teams:
            with open(self.aws_usage_multiple_file[teams.index(team)], "r") as f:
                valid_output[team] = f.read()

        self.assertEqual(aws_graph.create(usage_list=self.aws_usage_multiple), valid_output)
