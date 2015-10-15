#!/usr/bin/env python

import datetime


class AwsUsage:

    def __init__(self, access_key_id, secret_access_key):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    @staticmethod
    def get():
        return {"team1":
                {"date": [datetime.datetime(2015, 10, 1, 1, 0, 0),
                          datetime.datetime(2015, 10, 1, 2, 0, 0),
                          datetime.datetime(2015, 10, 2, 1, 0, 0),
                          datetime.datetime(2015, 10, 3, 1, 0, 0),
                          datetime.datetime(2015, 10, 3, 3, 0, 0)],
                 "cost": [3.00, 0.33, 0.50, 1.50, 0.25]},
                "team2":
                {"date": [datetime.datetime(2015, 10, 1, 4, 0, 0),
                          datetime.datetime(2015, 10, 1, 5, 0, 0),
                          datetime.datetime(2015, 10, 2, 1, 0, 0),
                          datetime.datetime(2015, 10, 3, 1, 0, 0),
                          datetime.datetime(2015, 10, 3, 1, 0, 0)],
                 "cost": [2.50, 2.50, 0.50, 1.50, 0.75]},
                "team3":
                {"date": [datetime.datetime(2015, 10, 3, 3, 0, 0),
                          datetime.datetime(2015, 10, 3, 1, 0, 0),
                          datetime.datetime(2015, 10, 1, 1, 0, 0),
                          datetime.datetime(2015, 10, 1, 2, 0, 0),
                          datetime.datetime(2015, 10, 2, 5, 0, 0)],
                 "cost": [2.00, 2.25, 0.12, 0.13, 1.50]},
                }
