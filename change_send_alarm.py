import json
import boto3

client = boto3.client('iot-data', region_name='us-east-1')

def lambda_handler(event, context):
    # TODO implement
    response = client.publish(
        topic='ESP32test/ChangeSendAlarm',
        qos=1,
        payload=json.dumps({"message":"change send alarm"})
    )
    return {
        'statusCode': 200,
        'body': json.dumps('Published to topic')
    }