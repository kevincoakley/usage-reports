#!/usr/bin/env python

try:
    from setuptools import setup
    extra = dict(install_requires=[
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


setup(name="databricks-usage-reports-scripts",
      version="0.0.1",
      description="Create usage report for Databricks service",
      long_description=readme(),
      author="Kevin Coakley",
      author_email="kcoakley@sdsc.edu",
      scripts=[
      ],
      url="",
      packages=[
          "databricksusagereport",
          "databricksusagereport/aws",
          "databricksusagereport/databricks",
      ],
      package_data={
          "databricksusagereport": ["templates/databricks-graph-data.js"],
          "databricksusagereport": ["templates/graph-data.js"],
      },
      platforms="Posix; MacOS X",
      classifiers=[
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.7",
      ],
      **extra
      )
