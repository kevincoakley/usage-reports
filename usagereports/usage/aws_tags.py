#!/usr/bin/env python

import re
import csv
import logging
import zipfile
import StringIO
import datetime
from usagereports.storage.s3 import S3


class AwsTagsUsage:

    def __init__(self):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)

    def get_current(self, bucket):
        self.logger.info("Started get_current")

        path_base = "846273844940-aws-billing-detailed-line-items-with-resources-and-tags"

        path = "%s-%s-%s.csv.zip" % (path_base,
                                     datetime.datetime.now().strftime("%Y"),
                                     datetime.datetime.now().strftime("%m"))

        return AwsTagsUsage.get(self, bucket, path)

    def get(self, bucket, path):
        self.logger.info("Started get")
        self.logger.info("AWS log path: %s", path)

        f = StringIO.StringIO()

        storage = S3()
        f.write(storage.download(bucket, path))

        f.seek(0)
        zip_file = zipfile.ZipFile(f, "r")
        if path[:-4] in zip_file.namelist():
            self.logger.info("CSV file found zipfile: %s", path[:-4])
            file_content = zip_file.read(path[:-4])
            return AwsTagsUsage.parse(self, file_content)

    def parse(self, csv_string):
        self.logger.info("Started parse")
        buf = StringIO.StringIO(csv_string)
        line = csv.DictReader(buf, delimiter=',')

        aws_usage_dict = dict()

        if "user:Cluster" in line.fieldnames or "user:cluster" in line.fieldnames \
                or "user:Course" in line.fieldnames or "user:course" in line.fieldnames \
                or "user:ClusterName" in line.fieldnames or "user:clustername" in line.fieldnames:
            self.logger.debug("user:cluster, user:clustername and user:course"
                              " exists in CSV fieldnames")

            for row in line:

                name = None

                # Only process rows that are of type LineItem
                if row['RecordType'] == "LineItem":

                    if "user:Cluster" in line.fieldnames:
                        if row['user:Cluster'] is not "":
                            name = re.sub("[^A-Za-z0-9]", "_", row["user:Cluster"])

                    if "user:cluster" in line.fieldnames:
                        if row['user:cluster'] is not "":
                            name = re.sub("[^A-Za-z0-9]", "_", row["user:cluster"])

                    if "user:Course" in line.fieldnames:
                        if row['user:Course'] is not "":
                            name = re.sub("[^A-Za-z0-9]", "_", row["user:Course"])

                    if "user:course" in line.fieldnames:
                        if row['user:course'] is not "":
                            name = re.sub("[^A-Za-z0-9]", "_", row["user:course"])

                    if "user:ClusterName" in line.fieldnames:
                        if row['user:ClusterName'] is not "":
                            name = re.sub("[^A-Za-z0-9]", "_", row["user:ClusterName"])

                    if "user:clustername" in line.fieldnames:
                        if row['user:clustername'] is not "":
                            name = re.sub("[^A-Za-z0-9]", "_", row["user:clustername"])

                    if "LinkedAccountId" in line.fieldnames:
                        if row['LinkedAccountId'] != "846273844940" and \
                                row['LinkedAccountId'] is not "":
                            name = "aws%s" % row["LinkedAccountId"]

                if name is not None:

                    # Everything in the tag before the _ is the name used for the graph
                    self.logger.debug("Tag Name: Before: %s After %s", name, name.split("_")[0])
                    name = name.split("_")[0]

                    # Cluster or course is not in aws_usage_dict
                    if name not in aws_usage_dict.keys():
                        self.logger.debug("Cluster or course %s not in aws_usage_dict", name)
                        aws_usage_dict[name] = {"date": [datetime.datetime.
                                                         strptime(row['UsageStartDate'][:10],
                                                                  '%Y-%m-%d')],
                                                "cost":
                                                    [float("{0:.02f}".format(
                                                        float(row["BlendedCost"])))]}

                    # Cluster or course and date are in aws_usage_dict
                    elif name in aws_usage_dict.keys() and \
                        datetime.datetime.strptime(row['UsageStartDate'][:10], '%Y-%m-%d') \
                            in aws_usage_dict[name]["date"]:
                        self.logger.debug("Cluster or course %s and %s in aws_usage_dict", name,
                                          datetime.datetime.strptime(row['UsageStartDate']
                                                                     [:10], '%Y-%m-%d'))
                        date_index = aws_usage_dict[name]['date'].\
                            index(datetime.datetime.strptime(row['UsageStartDate'][:10],
                                                             '%Y-%m-%d'))
                        date_cost = float(aws_usage_dict[name]["cost"]
                                          [date_index]) + float(row["BlendedCost"])
                        aws_usage_dict[name]["cost"][date_index] = float("{0:.02f}".format
                                                                         (float(date_cost)))

                    # Cluster or course is in aws_usage_dict but date is not
                    else:
                        self.logger.debug("Cluster or course %s is in aws_usage_dict but the "
                                          "date %s is not",
                                          name,
                                          datetime.datetime.strptime(row['UsageStartDate']
                                                                     [:10], '%Y-%m-%d'))
                        aws_usage_dict[name]["date"].append(datetime.datetime.
                                                            strptime(row['UsageStartDate'][:10],
                                                                     '%Y-%m-%d'))
                        aws_usage_dict[name]["cost"].append(float("{0:.02f}".format
                                                                  (float(row["BlendedCost"]))))

        else:
            self.logger.debug("user:cluster or user:course does not exist in CSV fieldnames")

        self.logger.debug("aws_usage_dict: %s", aws_usage_dict)

        return aws_usage_dict
