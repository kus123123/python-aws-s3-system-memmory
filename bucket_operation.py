import os
import boto3

aws_access_key_id = os.environ.get('AWS_ACCESS_KEY_ID')
aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY')

# Use the credentials to create an AWS service client using Boto3
s3_client = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

# s3_client.create_bucket(Bucket='new1212eq')  # bucket names must be unique
# s3_client.upload_file('test.txt', 'new1212eq', 'test.txt')  # upload a new file
# s3_client.upload_file('test.txt', 'new1212eq', 'test2.txt')  # upload a new file
# s3_client.download_file('new1212eq', 'test.txt', 'test3.txt')  # download a file
# s3_client.delete_object(Bucket='new1212eq', Key='test.txt')  # delete a file
# s3_client.delete_bucket(Bucket='new1212eq')  # delete a bucket
# s3_client.list_buckets()  # get a list of buckets
s3_client.list_objects(Bucket='new1212eq')  # get a list of objects in a bucket
# print all buckets
for bucket in s3_client.list_buckets()['Buckets']:
    print(bucket['Name'])


# Now you can use the 's3_client' object to interact with AWS S3
