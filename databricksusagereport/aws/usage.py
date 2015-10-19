#!/usr/bin/env python

import re
import csv
import boto
import zipfile
import StringIO
import datetime
from boto.s3.key import Key


class AwsUsage:

    bucket = "dse-billing"
    path_base = "846273844940-aws-billing-detailed-line-items-with-resources-and-tags"

    def __init__(self, access_key_id, secret_access_key):
        self.aws_access_key_id = access_key_id
        self.aws_secret_access_key = secret_access_key

    def get(self):
        s3_conn = boto.connect_s3(aws_access_key_id=self.aws_access_key_id,
                                  aws_secret_access_key=self.aws_secret_access_key)

        path = "%s-%s-%s.csv.zip" % \
               (AwsUsage.path_base,
                datetime.datetime.now().strftime("%Y"),
                datetime.datetime.now().strftime("%m"))

        bucket = s3_conn.get_bucket(AwsUsage.bucket)

        k = Key(bucket)
        k.key = path
        if k.exists():
            f = StringIO.StringIO()
            k.get_file(f)
            f.seek(0)
            gzf = zipfile.ZipFile(f, "r")
            if path[:-4] in gzf.namelist():
                file_content = gzf.read(path[:-4])
                return AwsUsage.parse(file_content)
        else:
            return None

    @staticmethod
    def parse(csv_string):
        buf = StringIO.StringIO(csv_string)
        line = csv.DictReader(buf, delimiter=',')

        return_dict = dict()

        for row in line:
            if row['user:Cluster'] is not "":
                name = re.sub("[^A-Za-z0-9]", "_", row["user:Cluster"])

                # Cluster is not in return_dict
                if name not in return_dict.keys():
                    return_dict[name] = {"date": [datetime.datetime.
                                                  strptime(row['UsageStartDate'][:7],
                                                           '%m/%d/%y')],
                                         "cost": [float("{0:.02f}".format(float(row["Cost"])))]}

                # Cluster and date are in return_dict
                elif name in return_dict.keys() and \
                    datetime.datetime.strptime(row['UsageStartDate']
                                               [:7], '%m/%d/%y') in return_dict[name]["date"]:

                    date_index = return_dict[name]['date'].\
                        index(datetime.datetime.strptime(row['UsageStartDate'][:7],
                                                         '%m/%d/%y'))

                    date_cost = float(return_dict[name]["cost"]
                                      [date_index]) + float(row["Cost"])

                    return_dict[name]["cost"][date_index] = float("{0:.02f}".format
                                                                  (float(date_cost)))

                # Cluster is in return_dict but date is not
                else:
                    return_dict[name]["date"].append(datetime.datetime.
                                                     strptime(row['UsageStartDate'][:7],
                                                              '%m/%d/%y'))

                    return_dict[name]["cost"].append(float("{0:.02f}".format
                                                           (float(row["Cost"]))))

        return return_dict
