import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('py_mini_project')

def lambda_handler(event, context):
    
    
    table.update_item(
        Key={
            'py_id': event["py_id"],
        },
        UpdateExpression='SET roll_no = :data',
        ExpressionAttributeValues={
            ':data': event["roll_no"]
        }
    )
    
    return {
        'statusCode': 200,
        'body': "success"
    }
