import json
import boto3

client = boto3.client('iot-data', region_name='us-east-1')

def lambda_handler(event, context):
    # TODO implement
    response = client.publish(
        topic='ESP32test/GetScanner',
        qos=1,
        payload=json.dumps({"message":"request data"})
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Published to topic')
    }
