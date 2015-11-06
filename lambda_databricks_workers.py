import usagereports.databricksworkers


def lambda_handler(event, context):

    usagereports.databricksworkers.main("mas-dse-usage-reports")
