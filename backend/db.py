import boto3
from boto3.dynamodb.conditions import Key

TABLE_NAME = "wx_data"
# Creating the DynamoDB Client
dynamodb_client = boto3.client('dynamodb',
  aws_access_key_id='AKIA36XSOWSAE6HGSR7A',
  aws_secret_access_key='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',
  region_name='eu-north-1')

# Creating the DynamoDB Table Resource
dynamodb = boto3.resource('dynamodb', aws_access_key_id='AKIA36XSOWSAE6HGSR7A',
  aws_secret_access_key='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',
  region_name="eu-north-1")
table = dynamodb.Table(TABLE_NAME)

def getItem():
  response = table.scan()
  print(response["Items"][0])
  return response["Items"][0]

def getLastItems():
    response = table.scan()
    return response["Items"][1:11:1]
