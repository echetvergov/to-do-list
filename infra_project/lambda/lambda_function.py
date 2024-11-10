import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDynamoDBTable')

def handler(event, context):
    # Example: Put an item in the DynamoDB table
    table.put_item(
        Item={
            'id': '123',
            'data': 'Hello, CDK!'
        }
    )

    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Data has been inserted into DynamoDB!')
    }
