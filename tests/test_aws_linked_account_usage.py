import unittest
import datetime
from usagereports.usage.aws_tags import AwsTagsUsage


class AWSLinkedAccountUsageTestCase(unittest.TestCase):

    def setUp(self):
        self.maxDiff = None
        self.linked_account_aws_usage_csv_file_string = "tests/aws/aws-billing-detailed-line-" \
                                                        "items-with-resources-and-tags-blended-" \
                                                        "linked.csv"

        self.aws_usage_output = {"aws987654321098":
                                 {"date": [datetime.datetime(2015, 9, 30, 0, 0)],
                                  "cost": [0.20]},
                                 "aws123456789012":
                                 {"date": [datetime.datetime(2015, 9, 29, 0, 0),
                                           datetime.datetime(2015, 9, 30, 0, 0)],
                                  "cost": [1.44, 1.10]},
                                 "aws890123456789":
                                 {"date": [datetime.datetime(2015, 9, 30, 0, 0)],
                                  "cost": [0.88]}
                                 }

    def test_aws_linked_account(self):
        aws_usage = AwsTagsUsage()

        with open(self.linked_account_aws_usage_csv_file_string, "r") as f:
            valid_output = f.read()

        self.assertEqual(aws_usage.parse(valid_output), self.aws_usage_output)
