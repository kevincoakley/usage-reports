import unittest
import datetime
from databricksusagereport.graph.databricks import DataBricksGraph


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.db_usage_no_history_file = "tests/graph/databricks_usage_no_history.js"
        self.db_usage_no_history = [{"name": "team1",
                                     "NumWorkers": 4,
                                     "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                    {"name": "team2",
                                     "NumWorkers": 8,
                                     "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                    {"name": "team3",
                                     "NumWorkers": 6,
                                     "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]
        self.db_usage_with_history_file = "tests/graph/databricks_usage_with_history.js"
        self.db_usage_with_history_ordered = [{"name": "team1",
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
        self.db_usage_with_history_unordered = [{"name": "team1",
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

    def test_databricks_graph_no_history(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_usage_no_history_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_no_history), valid_ouput)

    def test_databricks_graph_with_history_ordered(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_usage_with_history_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_with_history_ordered), valid_ouput)

    def test_databricks_graph_with_history_unordered(self):
        databricks_graph = DataBricksGraph()

        with open(self.db_usage_with_history_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.db_usage_with_history_unordered), valid_ouput)
