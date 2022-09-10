import json

def lambda_handler(event, context):
    # Replace with your call to sagemaker inference endpoint
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
