#############
usage-reports
#############

.. image:: https://travis-ci.org/kevincoakley/usage-reports.svg?branch=master
    :target: https://travis-ci.org/kevincoakley/usage-reports


aws-tags-cost
=============

Creates a graph of daily AWS usage cost based on AWS the tags in the AWS Detailed Billing Report.


databricks-workers
==================

Creates a graph of the current number of workers in each Databricks cluster. Designed to run hourly.



Both scripts can either be installed as command line scripts and executed via a command line scheduler
(cron) or they can be used as an AWS Lambda function.



############
Requirements
############

aws-tags-cost
=============

(1) `AWS Detailed Billing Reports with Tags turned on <http://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/detailed-billing-reports.html#turnonreports>`_
(2) `S3 Bucket configured for Website Hosting <http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html>`_
(3) `S3 Bucket Listing Enabled for Website Bucket <https://github.com/rgrp/s3-bucket-listing/>`_


databricks-workers
==================
(1) Your IP address must be white listed for the Databricks API. Contact help@databricks.com to have your IP address whitelisted.
(2) `S3 Bucket configured for Website Hosting <http://docs.aws.amazon.com/AmazonS3/latest/dev/HowDoIWebsiteConfiguration.html>`_
(3) `S3 Bucket Listing Enabled for Website Bucket <https://github.com/rgrp/s3-bucket-listing/>`_


Note: aws-tags-cost and databricks-workers can use the same S3 Bucket for Website hosting


############
Command Line
############

(1) Install command line scripts from source (see below).
(2) Configure AWS Credentials for boto3:

    (1) Copy /config/boto3/_aws/* to ~/.aws/
    (2) Update config and credentials with valid values.
    
(3) Configure Databricks Credentials (only needed for databricks-workers):

    (1) Copy /config/environ.sh to a secure location.
    (2) Update environ.sh with your Datbricks username and password.
    (3) Run: source environ.sh


Install from source::

    $ git clone https://github.com/kevincoakley/usage-reports.git
    $ cd usage-reports
    $ python setup.py install


Remove via pip::

    $ pip uninstall usage-reports -y


##########
AWS Lambda
##########

How to create a zip package to use with AWS Lambda::


    git clone https://github.com/kevincoakley/usage-reports.git /path/to/usage-reports/

    mkdir /path/to/temp/
    virtualenv /path/to/temp/
    cd /path/to/temp/
    source bin/activate
    pip install /path/to/usage-reports/

    mkdir /path/to/lambda/
    cd /path/to/lambda/
    cp -R /path/to/temp/lib/python2.7/site-packages/* .
    cp /path/to/usage-reports/lambda_aws_cost.py lambda.py
    or
    cp /path/to/usage-reports/lambda_databricks_workers.py lambda.py
    zip -r lambda.zip *


