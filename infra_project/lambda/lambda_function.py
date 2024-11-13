import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDynamoDBTable')

def handler(event, context):
    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Hello Eugen. It is working')
    }
