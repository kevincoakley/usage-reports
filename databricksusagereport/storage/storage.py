#!/usr/bin/env python

import logging
from databricksusagereport.storage.github import StorageGitHub
from databricksusagereport.storage.aws import StorageAWS


class Storage:

    def __init__(self, aws_access_key_id=None, aws_secret_access_key=None, github_token=None):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.aws_access_key_id = aws_access_key_id
        self.aws_secret_access_key = aws_secret_access_key
        self.github_token = github_token

    def get_storage(self):
        if self.aws_access_key_id is not None and self.aws_secret_access_key is not None \
                and self.github_token is not None:
            self.logger.info("aws_access_key_id and aws_secret_access_key and github_token all set."
                             " Please set either aws or github credentials")
            return None
        elif self.aws_access_key_id is not None and self.aws_secret_access_key is not None:
            self.logger.debug("aws_access_key_id: %s", self.aws_access_key_id)
            self.logger.debug("aws_secret_access_key: %s", self.aws_secret_access_key[:3])
            return StorageAWS(self.aws_access_key_id, self.aws_secret_access_key)
        elif self.github_token is not None:
            self.logger.debug("github_token: %s", self.github_token[:3])
            return StorageGitHub(self.github_token)
        else:
            self.logger.info("Missing aws_access_key_id and aws_secret_access_key or github_token")
            return None
