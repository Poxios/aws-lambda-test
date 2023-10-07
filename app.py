from chalice import Chalice
import sys
import boto3


app = Chalice(app_name="wasasak")
sys.path.append("/opt")


@app.on_sqs_message(queue='arn:aws:sqs:ap-northeast-2:906389837735:my-queue')
def one(*args, **kwargs):
    print('first')

def two(*args, **kwargs):
    print('second')

def three(*args, **kwargs):
    print('third')

def dead(*args, **kwargs):
    print('imdead')
