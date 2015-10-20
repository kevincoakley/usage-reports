import unittest
import datetime
from databricksusagereport.usage.aws import AwsUsage


class AWSUsageTestCase(unittest.TestCase):

    def setUp(self):
        self.aws_usage_csv_file_string = "tests/aws/aws-billing-detailed-line-" \
                                         "items-with-resources-and-tags.csv"

        self.aws_usage_output = {"admin_c1":
                                 {"date": [datetime.datetime(2015, 9, 30, 0, 0)],
                                  "cost": [0.20]},
                                 "team1":
                                 {"date": [datetime.datetime(2015, 9, 29, 0, 0),
                                           datetime.datetime(2015, 9, 30, 0, 0)],
                                  "cost": [1.44, 1.10]},
                                 "Undefined":
                                 {"date": [datetime.datetime(2015, 9, 30, 0, 0)],
                                  "cost": [0.88]}
                                 }

    def test_aws_usage_file(self):
        aws_usage = AwsUsage("key", "secret")

        with open(self.aws_usage_csv_file_string, "r") as f:
            valid_output = f.read()

        self.assertEqual(aws_usage.parse(valid_output), self.aws_usage_output)
