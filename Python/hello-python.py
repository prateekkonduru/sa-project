import boto3
import datetime
import os

region = os.environ['AWS_REGIO']
id = os.environ['AWS_ACCESS_KEY_I']
key = os.environ['AWS_SECRET_ACCESS_KE']

TOPIC_ARN = os.environ['ARN_SNS']
MESSAGE = 'No lingering files found'

client = boto3.client('sns', region_name=region, aws_access_key_id=id, aws_secret_access_key=key)


def lambda_handler(event, context):
    bucket_name = "my-tf-test-bucket-prateekkonduru"
    current_day = datetime.datetime.today().weekday()
    if current_day == 6:
        s3 = boto3.client('s3')
        objects = s3.list_objects(Bucket=bucket_name)
        if 'Contents' in objects:
            for obj in objects['Contents']:
                s3.delete_object(Bucket=bucket_name, Key=obj['Key'])
            print("All objects deleted from the bucket.")
        if 'Contents' in objects:
            response = client.publish(TopicArn=TOPIC_ARN, Message=MESSAGE)
        else:
            print("The bucket is already empty.")
    else:
        print("Today is not Sunday, skipping execution.")
