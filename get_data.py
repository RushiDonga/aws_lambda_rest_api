import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('py_mini_project')

def lambda_handler(event, context):
    
    response = table.get_item(Key=event)
    item = response['Item']

    return {
        'statusCode': 200,
        'body': item
    }
