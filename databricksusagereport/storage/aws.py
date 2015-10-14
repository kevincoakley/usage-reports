#!/usr/bin/env python

import logging
import boto
from boto.s3.key import Key


class StorageAWS:

    bucket = "mas-dse-usage-reports"

    def __init__(self, aws_access_key_id, aws_secret_access_key):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key

    def download(self, path):
        self.logger.info("Started download")

        s3_conn = boto.connect_s3(aws_access_key_id=self.aws_access_key_id,
                                  aws_secret_access_key=self.aws_secret_access_key)

        bucket = s3_conn.get_bucket(StorageAWS.bucket)
        k = Key(bucket)
        k.key = path
        if k.exists():
            return k.get_contents_as_string()
        else:
            return None

    def upload(self, path, content):
        self.logger.info("Started upload")

        s3_conn = boto.connect_s3(aws_access_key_id=self.aws_access_key_id,
                                  aws_secret_access_key=self.aws_secret_access_key)

        bucket = s3_conn.get_bucket(StorageAWS.bucket)
        k = Key(bucket)
        k.key = path
        k.set_contents_from_string(content)
