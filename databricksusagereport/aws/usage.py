#!/usr/bin/env python

import datetime


class AwsUsage:

    def __init__(self, access_key_id, secret_access_key):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    @staticmethod
    def get():
        return [{"name": "team1",
                 "cost": 3.00,
                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                {"name": "team1",
                 "cost": 0.33,
                 "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                {"name": "team1",
                 "cost": 0.50,
                 "date": datetime.datetime(2015, 10, 2, 1, 0, 0)},
                {"name": "team1",
                 "cost": 1.50,
                 "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                {"name": "team3",
                 "cost": 2.00,
                 "date": datetime.datetime(2015, 10, 3, 3, 0, 0)},
                {"name": "team2",
                 "cost": 2.50,
                 "date": datetime.datetime(2015, 10, 1, 4, 0, 0)},
                {"name": "team2",
                 "cost": 2.50,
                 "date": datetime.datetime(2015, 10, 1, 5, 0, 0)},
                {"name": "team2",
                 "cost": 0.50,
                 "date": datetime.datetime(2015, 10, 2, 1, 0, 0)},
                {"name": "team2",
                 "cost": 1.50,
                 "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                {"name": "team3",
                 "cost": 2.25,
                 "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                {"name": "team2",
                 "cost": 0.75,
                 "date": datetime.datetime(2015, 10, 3, 1, 0, 0)},
                {"name": "team3",
                 "cost": 0.12,
                 "date": datetime.datetime(2015, 10, 1, 1, 0, 0)},
                {"name": "team3",
                 "cost": 0.13,
                 "date": datetime.datetime(2015, 10, 1, 2, 0, 0)},
                {"name": "team3",
                 "cost": 1.50,
                 "date": datetime.datetime(2015, 10, 2, 5, 0, 0)},
                {"name": "team1",
                 "cost": 0.25,
                 "date": datetime.datetime(2015, 10, 3, 3, 0, 0)}]
