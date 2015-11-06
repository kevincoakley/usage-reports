import urllib
import usagereports.awstagscost


def lambda_handler(event, context):
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['s3']['object']['key']).decode('utf8')

    print "Bucket: %s Key: %s" % (bucket, key)

    usagereports.awstagscost.main("mas-dse-usage-reports", bucket, key)
