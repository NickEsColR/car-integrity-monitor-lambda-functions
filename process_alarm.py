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
                        'body': 'Se detecto la apertura de puerta',
                        'title': 'Alarma detectada',
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
