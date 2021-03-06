import json
import unittest
import datetime
from usagereports.graph.databricks_workers import DatabricksWorkersGraph


class DatabricksWorkersGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.db_usage_single_file = "tests/graph/databricks_workers_usage_single.js"
        self.db_usage_single = [{"name": "team1",
                                 "numWorkers": 4,
                                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                {"name": "team2",
                                 "numWorkers": 8,
                                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                {"name": "team3",
                                 "numWorkers": 6,
                                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]
        self.db_usage_multiple_file = "tests/graph/databricks_workers_usage_multiple.js"
        self.db_usage_multiple = [{"name": "team1",
                                   "numWorkers": 4,
                                   "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                  {"name": "team2",
                                   "numWorkers": 10,
                                   "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                  {"name": "team3",
                                   "numWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 3, 0, 0)},
                                  {"name": "team1",
                                   "numWorkers": 4,
                                   "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                  {"name": "team2",
                                   "numWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                  {"name": "team3",
                                   "numWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                                  {"name": "team2",
                                   "numWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                  {"name": "team3",
                                   "numWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                  {"name": "team2",
                                   "numWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                  {"name": "team1",
                                   "numWorkers": 4,
                                   "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                                  {"name": "team1",
                                   "numWorkers": 6,
                                   "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                  {"name": "team3",
                                   "numWorkers": 8,
                                   "date": datetime.datetime(2015, 10, 1, 4, 0, 0)}]
        self.db_history_json_file = "tests/graph/history.json"
        self.db_usage_for_history = [{"name": "team1",
                                      "numWorkers": 6,
                                      "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                     {"name": "team2",
                                      "numWorkers": 8,
                                      "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                                     {"name": "team3",
                                      "numWorkers": 8,
                                      "date": datetime.datetime(2015, 10, 1, 4, 0, 0)}]

    def test_databricks_workers_graph_single(self):
        databricks_graph = DatabricksWorkersGraph()

        with open(self.db_usage_single_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(usage_list=self.db_usage_single), valid_ouput)

    def test_databricks_workers_graph_multiple(self):
        databricks_graph = DatabricksWorkersGraph()

        with open(self.db_usage_multiple_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(usage_list=self.db_usage_multiple), valid_ouput)

    def test_databricks_workers_graph_history(self):
        databricks_graph = DatabricksWorkersGraph()

        with open(self.db_history_json_file) as j:
            history_list = json.load(j)

        with open(self.db_usage_multiple_file, "r") as f:
            valid_ouput = f.read()

        self.assertEqual(databricks_graph.create(usage_list=self.db_usage_for_history,
                                                 history_list=history_list),
                         valid_ouput)
