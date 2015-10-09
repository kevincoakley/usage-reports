import os
import unittest
from databricksusagereport.storage.storage import Storage
from databricksusagereport.storage.github import StorageGitHub
from databricksusagereport.storage.aws import StorageAWS


class StorageTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_databricksworkers_get_storage_aws_and_github(self):
        os.environ["AWS_ACCESS_KEY_ID"] = "1234567890"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "abc123"
        os.environ["GITHUB_TOKEN"] = "1234567890"

        so = Storage()

        self.assertIsNone(so.get_storage())

    def test_databricksworkers_get_storage_none(self):
        if "AWS_ACCESS_KEY_ID" in os.environ:
            del os.environ["AWS_ACCESS_KEY_ID"]
        if "AWS_SECRET_ACCESS_KEY" in os.environ:
            del os.environ["AWS_SECRET_ACCESS_KEY"]
        if "GITHUB_TOKEN" in os.environ:
            del os.environ["GITHUB_TOKEN"]

        so = Storage()

        self.assertIsNone(so.get_storage())

    def test_databricksworkers_get_storage_github(self):
        os.environ["GITHUB_TOKEN"] = "1234567890"
        if "AWS_ACCESS_KEY_ID" in os.environ:
            del os.environ["AWS_ACCESS_KEY_ID"]
        if "AWS_SECRET_ACCESS_KEY" in os.environ:
            del os.environ["AWS_SECRET_ACCESS_KEY"]

        so = Storage()

        self.assertIsInstance(so.get_storage(), StorageGitHub)

    def test_databricksworkers_get_storage_aws(self):
        os.environ["AWS_ACCESS_KEY_ID"] = "1234567890"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "abc123"
        if "GITHUB_TOKEN" in os.environ:
            del os.environ["GITHUB_TOKEN"]

        so = Storage()

        self.assertIsInstance(so.get_storage(), StorageAWS)

    def test_databricksworkers_get_storage_aws_no_secret_key(self):
        os.environ["AWS_ACCESS_KEY_ID"] = "1234567890"
        if "AWS_SECRET_ACCESS_KEY" in os.environ:
            del os.environ["AWS_SECRET_ACCESS_KEY"]
        if "GITHUB_TOKEN" in os.environ:
            del os.environ["GITHUB_TOKEN"]

        so = Storage()

        self.assertIsNone(so.get_storage())
