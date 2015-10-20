#!/usr/bin/env python

import re
import csv
import boto
import logging
import zipfile
import StringIO
import datetime
from boto.s3.key import Key


class AwsUsage:

    bucket = "dse-billing"
    path_base = "846273844940-aws-billing-detailed-line-items-with-resources-and-tags"

    def __init__(self, access_key_id, secret_access_key):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.aws_access_key_id = access_key_id
        self.aws_secret_access_key = secret_access_key

    def get(self):
        self.logger.info("Started get")
        s3_conn = boto.connect_s3(aws_access_key_id=self.aws_access_key_id,
                                  aws_secret_access_key=self.aws_secret_access_key)

        path = "%s-%s-%s.csv.zip" % (AwsUsage.path_base,
                                     datetime.datetime.now().strftime("%Y"),
                                     datetime.datetime.now().strftime("%m"))
        self.logger.info("AWS log path: %s", path)

        bucket = s3_conn.get_bucket(AwsUsage.bucket)
        self.logger.info("AWS bucket: %s", AwsUsage.bucket)

        k = Key(bucket)
        k.key = path
        if k.exists():
            self.logger.info("Key exists on AWS: %s", path)
            f = StringIO.StringIO()
            k.get_file(f)
            f.seek(0)
            zip_file = zipfile.ZipFile(f, "r")
            if path[:-4] in zip_file.namelist():
                self.logger.info("CSV file found zipfile: %s", path[:-4])
                file_content = zip_file.read(path[:-4])
                return AwsUsage.parse(self, file_content)
        else:
            self.logger.info("Key does not exist on AWS: %s", path)
            return None

    def parse(self, csv_string):
        self.logger.info("Started parse")
        buf = StringIO.StringIO(csv_string)
        line = csv.DictReader(buf, delimiter=',')

        aws_usage_dict = dict()

        for row in line:
            if row['user:Cluster'] is not "":
                name = re.sub("[^A-Za-z0-9]", "_", row["user:Cluster"])

                # Cluster is not in aws_usage_dict
                if name not in aws_usage_dict.keys():
                    self.logger.info("Cluster %s not in aws_usage_dict", name)
                    aws_usage_dict[name] = {"date": [datetime.datetime.
                                                     strptime(row['UsageStartDate'][:10],
                                                              '%Y-%m-%d')],
                                            "cost": [float("{0:.02f}".format(float(row["Cost"])))]}

                # Cluster and date are in aws_usage_dict
                elif name in aws_usage_dict.keys() and \
                    datetime.datetime.strptime(row['UsageStartDate']
                                               [:10], '%Y-%m-%d') in aws_usage_dict[name]["date"]:
                    self.logger.info("Cluster %s and %s in aws_usage_dict", name,
                                     datetime.datetime.strptime(row['UsageStartDate']
                                                                [:10], '%Y-%m-%d'))
                    date_index = aws_usage_dict[name]['date'].\
                        index(datetime.datetime.strptime(row['UsageStartDate'][:10],
                                                         '%Y-%m-%d'))
                    date_cost = float(aws_usage_dict[name]["cost"]
                                      [date_index]) + float(row["Cost"])
                    aws_usage_dict[name]["cost"][date_index] = float("{0:.02f}".format
                                                                     (float(date_cost)))

                # Cluster is in aws_usage_dict but date is not
                else:
                    self.logger.info("Cluster %s is in aws_usage_dict but the date %s is not", name,
                                     datetime.datetime.strptime(row['UsageStartDate']
                                                                [:10], '%Y-%m-%d'))
                    aws_usage_dict[name]["date"].append(datetime.datetime.
                                                        strptime(row['UsageStartDate'][:10],
                                                                 '%Y-%m-%d'))
                    aws_usage_dict[name]["cost"].append(float("{0:.02f}".format
                                                              (float(row["Cost"]))))

        self.logger.debug("aws_usage_dict: %s", aws_usage_dict)

        return aws_usage_dict
