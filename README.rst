#############
usage-reports
#############

.. image:: https://travis-ci.org/kevincoakley/databricks-usage-report-scripts.svg?branch=master
    :target: https://travis-ci.org/kevincoakley/databricks-usage-report-scripts



How to create a zip package to use with AWS Lambda::

    mkdir /path/to/temp/
    virtualenv /path/to/temp/
    cd /path/to/temp/
    source bin/activate
    pip install /path/to/databricks-usage-report-scripts/

    mkdir /path/to/lambda/
    cd /path/to/lambda/
    cp -R /path/to/temp/lib/python2.7/site-packages/* .
    cp /path/to/databricks-usage-report-scripts/lambda_aws_cost.py lambda.py
    or
    cp /path/to/databricks-usage-report-scripts/lambda_databricks_workers.py lambda.py
    zip -r lambda.zip *


