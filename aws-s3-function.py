import boto3

s3=boto3.client('s3')

bucket_name='my-aws-python-buckt123'

file_path='/home/kus/Documents/python-aws-script/available-memmory.txt'

object_name='available-memmory.txt'

s3.upload_file(file_path,bucket_name,object_name)

print("File uploaded successfully")
