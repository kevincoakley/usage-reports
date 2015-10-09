#!/usr/bin/env python

import os
import logging
from databricksusagereport.storage.github import StorageGitHub
from databricksusagereport.storage.aws import StorageAWS


class Storage:

    def __init__(self):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)

    def get_storage(self):
        aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID", None)
        aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY", None)
        github_token = os.environ.get("GITHUB_TOKEN", None)

        if aws_access_key_id is not None and aws_secret_access_key is not None \
                and github_token is not None:
            self.logger.info("aws_access_key_id and aws_secret_access_key and github_token all set."
                             " Please set either aws or github credentials")
            return None
        elif aws_access_key_id is not None and aws_secret_access_key is not None:
            self.logger.debug("aws_access_key_id: %s", aws_access_key_id)
            self.logger.debug("aws_secret_access_key: %s", aws_secret_access_key[:3])
            return StorageAWS(aws_access_key_id, aws_secret_access_key)
        elif github_token is not None:
            self.logger.debug("github_token: %s", github_token[:3])
            return StorageGitHub(github_token)
        else:
            self.logger.info("Missing aws_access_key_id and aws_secret_access_key or github_token")
            return None
