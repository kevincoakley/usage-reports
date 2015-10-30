#!/usr/bin/env python

try:
    from setuptools import setup
    extra = dict(install_requires=[
        "github3.py>=1.0.0a2",
        "boto>=2.38.0",
    ],
        include_package_data=True,
        test_suite="tests.suite.load_tests",
    )
except ImportError:
    from distutils.core import setup
    extra = {}


def readme():
    with open("README.rst") as f:
        return f.read()


setup(name="databricks-usage-report-scripts",
      version="0.1.1",
      description="Create usage and cost reports for the Databricks service",
      long_description=readme(),
      author="Kevin Coakley",
      author_email="kcoakley@sdsc.edu",
      scripts=[
          "bin/databricks-workers",
          "bin/databricks-aws-cost",
      ],
      url="",
      packages=[
          "databricksusagereport",
          "databricksusagereport/graph",
          "databricksusagereport/storage",
          "databricksusagereport/usage",
      ],
      package_data={
          "databricksusagereport": ["templates/databricks-graph-data.js",
                                    "templates/graph-data.js",
                                    "html/index.html",
                                    "html/aws/index.html",
                                    ],
      },
      platforms="Posix; MacOS X",
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
      ],
      **extra
      )
