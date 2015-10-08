import unittest
import datetime
from databricksusagereport.graph.aws import AWSGraph


class AWSGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.aws_usage_single_file = ["tests/graph/aws_usage_single.js"]
        self.aws_usage_single = [{"name": "team1",
                                  "cost": 1.00,
                                  "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                 {"name": "team1",
                                  "cost": 1.25,
                                  "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                 {"name": "team1",
                                  "cost": .75,
                                  "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                 {"name": "team1",
                                  "cost": .50,
                                  "date": datetime.datetime(2015, 10, 2, 1, 0, 0)},
                                 {"name": "team1",
                                  "cost": .50,
                                  "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                                 {"name": "team1",
                                  "cost": .33,
                                  "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                 {"name": "team1",
                                  "cost": 1.25,
                                  "date": datetime.datetime(2015, 10, 3, 1, 0, 0)}]
        self.aws_usage_multiple_file = ["tests/graph/aws_usage_multiple_1.js",
                                        "tests/graph/aws_usage_multiple_2.js",
                                        "tests/graph/aws_usage_multiple_3.js"]
        self.aws_usage_multiple = [{"name": "team1",
                                    "cost": 3.00,
                                    "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                   {"name": "team1",
                                    "cost": 0.33,
                                    "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                   {"name": "team1",
                                    "cost": 0.50,
                                    "date": datetime.datetime(2015, 10, 2, 1, 0, 0)},
                                   {"name": "team1",
                                    "cost": 1.50,
                                    "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                                   {"name": "team3",
                                    "cost": 2.00,
                                    "date": datetime.datetime(2015, 10, 3, 3, 0, 0)},
                                   {"name": "team2",
                                    "cost": 2.50,
                                    "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                   {"name": "team2",
                                    "cost": 2.50,
                                    "date": datetime.datetime(2015, 10, 1, 5, 0, 0)},
                                   {"name": "team2",
                                    "cost": 0.50,
                                    "date": datetime.datetime(2015, 10, 2, 1, 0, 0)},
                                   {"name": "team2",
                                    "cost": 1.50,
                                    "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                                   {"name": "team3",
                                    "cost": 2.25,
                                    "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                                   {"name": "team2",
                                    "cost": 0.75,
                                    "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                                   {"name": "team3",
                                    "cost": 0.12,
                                    "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                   {"name": "team3",
                                    "cost": 0.13,
                                    "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                   {"name": "team3",
                                    "cost": 1.50,
                                    "date": datetime.datetime(2015, 10, 2, 5, 0, 0)},
                                   {"name": "team1",
                                    "cost": 0.25,
                                    "date": datetime.datetime(2015, 10, 3, 3, 0, 0)}]

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
