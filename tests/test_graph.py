import json
import unittest
import datetime
from databricksusagereport.graph.databricks import DataBricksGraph


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.db_usage_single_file = "tests/graph/databricks_usage_single.js"
        self.db_usage_single = [{"name": "team1",
                                 "NumWorkers": 4,
                                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                {"name": "team2",
                                 "NumWorkers": 8,
                                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                {"name": "team3",
                                 "NumWorkers": 6,
                                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]
        self.db_usage_multiple_file = "tests/graph/databricks_usage_multiple.js"
        self.db_usage_multiple = [{"name": "team1",
                                   "NumWorkers": 4,
                                   "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                  {"name": "team2",
                                   "NumWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                  {"name": "team3",
                                   "NumWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                  {"name": "team1",
                                   "NumWorkers": 4,
                                   "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                  {"name": "team2",
                                   "NumWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                  {"name": "team3",
                                   "NumWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                  {"name": "team1",
                                   "NumWorkers": 4,
                                   "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                  {"name": "team2",
                                   "NumWorkers": 10,
                                   "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                  {"name": "team3",
                                   "NumWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                  {"name": "team1",
                                   "NumWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                  {"name": "team2",
                                   "NumWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                  {"name": "team3",
                                   "NumWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 4, 0, 0)}]
        self.db_usage_multiple_unordered = [{"name": "team1",
                                             "NumWorkers": 4,
                                             "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                            {"name": "team2",
                                             "NumWorkers": 10,
                                             "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                            {"name": "team3",
                                             "NumWorkers": 6,
                                             "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                            {"name": "team1",
                                             "NumWorkers": 4,
                                             "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                            {"name": "team2",
                                             "NumWorkers": 8,
                                             "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                            {"name": "team3",
                                             "NumWorkers": 6,
                                             "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                            {"name": "team2",
                                             "NumWorkers": 6,
                                             "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                            {"name": "team3",
                                             "NumWorkers": 8,
                                             "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                            {"name": "team2",
                                             "NumWorkers": 8,
                                             "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                            {"name": "team1",
                                             "NumWorkers": 4,
                                             "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                            {"name": "team1",
                                             "NumWorkers": 6,
                                             "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                            {"name": "team3",
                                             "NumWorkers": 8,
                                             "date": datetime.datetime(2015, 10, 1, 4, 0, 0)}]
        self.db_history_json_file = "tests/graph/history.json"
        self.db_usage_for_history = [{"name": "team1",
                                      "NumWorkers": 6,
                                      "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                     {"name": "team2",
                                      "NumWorkers": 8,
                                      "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                     {"name": "team3",
                                      "NumWorkers": 8,
                                      "date": datetime.datetime(2015, 10, 1, 4, 0, 0)}]
        self.aws_usage = [{"name": "team1",
                           "Cost": 1.00,
                           "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                          {"name": "team1",
                           "Cost": 1.00,
                           "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]

    def test_databricks_graph_single(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_usage_single_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_single), valid_ouput)

    def test_databricks_graph_multiple(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_usage_multiple_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_multiple), valid_ouput)

    def test_databricks_graph_multiple_unordered(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_usage_multiple_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_multiple_unordered), valid_ouput)

    def test_databricks_graph_history(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_history_json_file) as j:
            history_list = json.load(j)

        with open(self.db_usage_multiple_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_for_history, history_list),
                         valid_ouput)