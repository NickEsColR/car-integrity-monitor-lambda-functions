#this is the function for aws lambda that notify with sns when function is triggered
#import aws-sdk
import boto3
import json

#sns configuration
sns = boto3.client('sns')
#function activated by lambda function
def lambda_handler(event,context):
        #sns
        target_arn = 'arn to publish'
        payload = {
                'default': 'default',
                'GCM':{
                'notification':{
                        'body': event,
                        'title': 'Scanner',
                        'sound': 'default'
                }
                }
        } 
        payload['GCM'] = json.dumps(payload['GCM'])
        payload = json.dumps(payload)
        response = sns.publish(TargetArn=target_arn,Message=payload,MessageStructure='json')
        return {
                'statusCode': 200,
                'body': json.dumps(response)
        }
