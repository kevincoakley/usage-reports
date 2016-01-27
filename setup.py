#!/usr/bin/env python

try:
    from setuptools import setup
    extra = dict(install_requires=[
        "boto3>=1.2",
        "botocore>=1.3",
        "requests>=2.8",
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


setup(name="usage-reports",
      version="0.2.2",
      description="Create usage and cost reports for AWS and Databricks services",
      long_description=readme(),
      author="Kevin Coakley",
      author_email="kcoakley@sdsc.edu",
      scripts=[
          "bin/databricks-workers",
          "bin/aws-tags-cost",
      ],
      url="",
      packages=[
          "usagereports",
          "usagereports/graph",
          "usagereports/storage",
          "usagereports/usage",
      ],
      package_data={
          "usagereports": ["templates/graph-data.js",
                           "templates/data.js",
                           "html/graph/index.html",
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
