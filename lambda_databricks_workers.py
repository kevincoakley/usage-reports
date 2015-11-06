import databricksusagereport.databricksworkers


def lambda_handler(event, context):

    databricksusagereport.databricksworkers.main("mas-dse-usage-reports")
