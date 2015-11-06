#!/usr/bin/env python

import logging
import boto3
from botocore import exceptions as botocore_exceptions
from pkg_resources import resource_string


class S3:

    def __init__(self):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)

    def download(self, bucket, path):
        self.logger.info("Started download")

        s3 = boto3.resource('s3')

        if s3.Bucket(bucket) in s3.buckets.all():
            key = s3.Object(bucket, path)
            try:
                self.logger.debug("AWS key exists: %s", path)
                return key.get()["Body"].read()
            except botocore_exceptions.ClientError, e:
                if e.response['Error']['Code'] == "NoSuchKey":
                    self.logger.debug("AWS key does not exist: %s", path)
                    return None
                else:
                    self.logger.info("Unknown download error: %s", path)
                    return None
        else:
            self.logger.info("Bucket not found: %s", bucket)

    def upload(self, bucket, path, content):
        self.logger.info("Started upload")
        content_type = 'text/html'

        s3 = boto3.resource('s3')

        if s3.Bucket(bucket) in s3.buckets.all():
            key = s3.Object(bucket, path)
            key.put(Body=content, ContentType=content_type)
        else:
            self.logger.info("Bucket not found: %s", bucket)

    def upload_index(self, bucket, path):
        self.logger.info("Upload index file")

        data_bricks_usage_file = resource_string("usagereports", "html/aws/index.html")

        aws_paths = []
        split_path = path.split("/")
        for index, dirs in enumerate(split_path):
            if index == 0:
                aws_paths.append(split_path[index])

            else:
                aws_paths.append("%s/%s" % (aws_paths[index - 1], split_path[index]))

        self.logger.debug("AWS Paths: ", aws_paths)

        for directory in aws_paths:
            download = self.download(bucket, "%s/index.html" % directory)

            if download is None:
                self.logger.info("Uploading index: %s/index.html", directory)
                self.upload(bucket, "%s/index.html" % directory, data_bricks_usage_file)
