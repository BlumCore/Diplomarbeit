from flask import Flask, render_template
from datetime import datetime
import boto3
from boto3.dynamodb.conditions import Key

app = Flask(__name__,  template_folder='templates')

@app.route('/', methods=["GET"])
def index():
    item = getItem()
    lastimes = getLastItems()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return render_template("index.html", item=item, old=lastimes, time=current_time)

@app.route('/history')
def history():
    item = getItem()
    lastimes = getLastItems()
    return render_template("history.html", item=item, old=lastimes)

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

@app.route('/getItem', methods=["GET"])
def getItem():
  response = table.query(
    KeyConditionExpression=Key("device").eq("1"),
    ScanIndexForward=False,
    Limit=1
  )
  return response["Items"][0]

def getLastItems():
  response = table.query(
    KeyConditionExpression=Key("device").eq("1"),
    ScanIndexForward=False,
    Limit=10
  )
  return response["Items"]
