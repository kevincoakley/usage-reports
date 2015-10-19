#!/usr/bin/env python

import datetime
import re
import csv
import StringIO


class AwsUsage:

    def __init__(self, access_key_id, secret_access_key):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    def parse(self, csv_file_string):
        buf = StringIO.StringIO(csv_file_string)
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
