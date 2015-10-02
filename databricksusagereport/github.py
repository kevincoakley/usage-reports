#!/usr/bin/env python

import os.path
import logging
# noinspection PyPackageRequirements
import github3


class GitHub:

    user = "kevincoakley"
    repository = "databricks-usage-report"

    def __init__(self, token):
        name = '.'.join([__name__, self.__class__.__name__])
        self.logger = logging.getLogger(name)
        self.token = token

    def download(self, path):
        self.logger.info("Started download")

        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        github = github3.login(token=self.token)

        repo = github.repository(GitHub.user, GitHub.repository)

        directory_contents = repo.directory_contents(directory)
        self.logger.debug("directory_contents: %s", directory_contents)

        for content in directory_contents:

            if content[0] == filename:
                return repo.blob(content[1].sha).decoded

        return None

    def upload(self, path, content):
        self.logger.info("Started upload")
        commit_comment = "Automated Commit: %s" % path
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        github = github3.login(token=self.token)

        repo = github.repository(GitHub.user, GitHub.repository)

        directory_contents = repo.directory_contents(directory)
        self.logger.debug("directory_contents: %s", directory_contents)

        github_file = None

        for directory_item in directory_contents:

            if directory_item[0] == filename:
                github_file = directory_item[1]

        if github_file is None:
            self.logger.info("Uploading new file: %s", path)
            self.logger.debug("Content: %s", content)
            repo.create_file(path, commit_comment, content.encode('utf-8'))
        else:
            self.logger.info("Updating existing file: %s", path)
            self.logger.debug("Content: %s", content)
            github_file.update(commit_comment, content.encode('utf-8'))
