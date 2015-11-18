import os
import usagereports.databricksworkers
import lambda_databricks_secrets


def lambda_handler(event, context):
    os.environ['DATABRICKS_USERNAME'] = lambda_databricks_secrets.databricks_username
    os.environ['DATABRICKS_PASSWORD'] = lambda_databricks_secrets.databricks_password

    usagereports.databricksworkers.main("mas-dse-usage-reports")
