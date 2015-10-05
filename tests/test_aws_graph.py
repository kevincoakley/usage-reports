import unittest
import datetime


class AWSGraphTestCase(unittest.TestCase):

    def setUp(self):
        self.aws_usage = [{"name": "team1",
                           "cost": 1.00,
                           "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                          {"name": "team1",
                           "cost": 1.00,
                           "date": datetime.datetime(2015, 10, 1, 1, 0, 0)}]
