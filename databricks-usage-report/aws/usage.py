#!/usr/bin/env python


class AwsUsage:

    def __init__(self, access_key_id, secret_access_key):
        self.access_key_id = access_key_id
        self.secret_access_key = secret_access_key

    def get(self):
        return dict()
