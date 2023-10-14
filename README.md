**Project Name: AWS S3 Memory Monitoring**
Description:
This project consists of two components: a Python script and a shell script. The Python script creates an Amazon S3 bucket using the Boto3 library and uploads a text file containing available memory information. The shell script records available memory before and after clearing cache, storing the results in a text file. The text file is then uploaded to the S3 bucket. The project is automated using crontab to run daily at 12:00 AM.
**Installation:**

**Clone the Repository**
git clone 
cd aws-s3-bucket-creator
