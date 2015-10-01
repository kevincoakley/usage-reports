#!/usr/bin/env python

import os.path
# noinspection PyPackageRequirements
import github3


class GitHub:

    user = "kevincoakley"
    repository = "databricks-usage-report"

    def __init__(self, token):
        self.token = token

    def download(self, path):
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        github = github3.login(token=self.token)

        repo = github.repository(GitHub.user, GitHub.repository)

        directory_contents = repo.directory_contents(directory)

        for content in directory_contents:

            if content[0] == filename:
                return repo.blob(content[1].sha).decoded

        return None

    def upload(self, path, content):
        commit_comment = "Automated Commit: %s" % path
        filename = os.path.basename(path)
        directory = os.path.dirname(path)

        github = github3.login(token=self.token)

        repo = github.repository(GitHub.user, GitHub.repository)

        directory_contents = repo.directory_contents(directory)

        github_file = None

        for content in directory_contents:

            if content[0] == filename:
                github_file = content[1]

        if github_file is None:
            repo.create_file(path, commit_comment, content)
        else:
            github_file.update(commit_comment, content)
