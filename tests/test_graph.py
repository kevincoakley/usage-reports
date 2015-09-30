import unittest
import datetime
from databricksusagereport.graph import Graph


class GraphTestCase(unittest.TestCase):

    def setUp(self):
        self.databricks_usage_no_history_file = "tests/graph/databricks_usage_no_history.js"
        self.databricks_usage_no_history = [{"name": "team1",
                                             "NumWorkers": 4,
                                             "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                            {"name": "team2",
                                             "NumWorkers": 8,
                                             "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                            {"name": "team3",
                                             "NumWorkers": 6,
                                             "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]
        self.aws_usage = [{"name": "team1",
                           "Cost": 1.00,
                           "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                          {"name": "team1",
                           "Cost": 1.00,
                           "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]

    def test_databricks_graph_no_history(self):
        databricks_graph = Graph()

        with open(self.databricks_usage_no_history_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(self.databricks_usage_no_history), valid_ouput)
