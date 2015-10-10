import unittest
from databricksusagereport.storage.storage import Storage
from databricksusagereport.storage.github import StorageGitHub
from databricksusagereport.storage.aws import StorageAWS


class StorageTestCase(unittest.TestCase):

    def setUp(self):
        self.aws_access_key_id = "1234567890"
        self.aws_secret_access_key = "abc123"
        self.github_token = "1234567890"

    def test_databricksworkers_get_storage_aws_and_github(self):
        so = Storage(aws_access_key_id=self.aws_access_key_id,
                     aws_secret_access_key=self.aws_secret_access_key,
                     github_token=self.github_token)

        self.assertIsNone(so.get_storage())

    def test_databricksworkers_get_storage_none(self):
        so = Storage(aws_access_key_id=None,
                     aws_secret_access_key=None,
                     github_token=None)

        self.assertIsNone(so.get_storage())

    def test_databricksworkers_get_storage_github(self):
        so = Storage(aws_access_key_id=None,
                     aws_secret_access_key=None,
                     github_token=self.github_token)

        self.assertIsInstance(so.get_storage(), StorageGitHub)

    def test_databricksworkers_get_storage_aws(self):
        so = Storage(aws_access_key_id=self.aws_access_key_id,
                     aws_secret_access_key=self.aws_secret_access_key,
                     github_token=None)

        self.assertIsInstance(so.get_storage(), StorageAWS)

    def test_databricksworkers_get_storage_aws_no_secret_key(self):
        so = Storage(aws_access_key_id=self.aws_access_key_id,
                     aws_secret_access_key=None,
                     github_token=None)

        self.assertIsNone(so.get_storage())
