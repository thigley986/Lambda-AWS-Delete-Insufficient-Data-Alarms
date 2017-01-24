import boto3
import sys
import time

#AWS Account and Region Definition for Reboot Actions
akid = 'ACCOUNT_ID'
region = 'REGION'

#Create Session with IAM User
session = boto3.session.Session(aws_access_key_id='ACCESS_KEY_ID', aws_secret_access_key='ACCESS_KEY_SECRET')

#Create AWS clients
cw = session.client('cloudwatch')

def lambda_handler(event, context):
     
    response = cw.describe_alarms(
        StateValue='INSUFFICIENT_DATA'
      )
     
    alarms = response['MetricAlarms']
    for alarm in alarms:
        try:
            alarm_name = alarm['AlarmName']
            print alarm_name
            cw.delete_alarms(
            AlarmNames=[alarm_name]
            )
            
        except Exception, e:
            print ("Error Encountered.")
            print (e)
            time.sleep(2)
