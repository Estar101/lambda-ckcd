import json

def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from CICD Lambda! github actions workflow vscode')
    }