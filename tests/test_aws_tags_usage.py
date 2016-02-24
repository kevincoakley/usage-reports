import unittest
import datetime
from usagereports.usage.aws_tags import AwsTagsUsage


class AWSTagsUsageTestCase(unittest.TestCase):

    def setUp(self):
        self.aws_usage_csv_cluster_file_string = "tests/aws/aws-billing-detailed-line-" \
                                                 "items-with-resources-and-tags-blended-cluster.csv"
        self.aws_usage_csv_course_file_string = "tests/aws/aws-billing-detailed-line-" \
                                                "items-with-resources-and-tags-blended-course.csv"
        self.no_cluster_aws_usage_csv_file_string = "tests/aws/aws-billing-detailed-line-items-" \
                                                    "with-resources-and-tags-blended-missing-" \
                                                    "tags.csv"

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

    def test_aws_tags_cluster_usage_file(self):
        aws_usage = AwsTagsUsage()

        with open(self.aws_usage_csv_cluster_file_string, "r") as f:
            valid_output = f.read()

        self.assertEqual(aws_usage.parse(valid_output), self.aws_usage_output)

    def test_aws_tags_course_usage_file(self):
        aws_usage = AwsTagsUsage()

        with open(self.aws_usage_csv_course_file_string, "r") as f:
            valid_output = f.read()

        self.assertEqual(aws_usage.parse(valid_output), self.aws_usage_output)

    def test_aws_tags_usage_file_no_cluster_tag(self):
        aws_usage = AwsTagsUsage()

        with open(self.no_cluster_aws_usage_csv_file_string, "r") as f:
            valid_output = f.read()

        self.assertEqual(aws_usage.parse(valid_output), {})
