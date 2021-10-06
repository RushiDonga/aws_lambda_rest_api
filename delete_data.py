import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('py_mini_project')

def lambda_handler(event, context):
    
    response = table.delete_item(Key=event)

    return {
        'statusCode': 200,
        'body': "success",
        "response":response,
    }
