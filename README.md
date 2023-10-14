# Project Name: AWS S3 Memory Monitoring

![image](https://app.eraser.io/workspace/ubEdoBw2qrzpGaJlDyeH?origin=share&elements=mih5-bGQ4S_AR1jxmjmgeg)

## Description:
This project consists of two components: a Python script and a shell script. The Python script creates an Amazon S3 bucket using the Boto3 library and uploads a text file containing available memory information. The shell script records available memory before and after clearing cache, storing the results in a text file. The text file is then uploaded to the S3 bucket. The project is automated using crontab to run daily at 12:00 AM.

## Installation:
1. **Prerequisites:**
   - Python installed on your system
   - AWS credentials configured with appropriate permissions
   - Boto3 library installed:
     ```
     pip install boto3
     ```
2. **Clone the Repository:**
   ```
   git clone <repository_url>
   cd aws-memory-monitoring
   ```

## Usage:
1. **Set Up AWS Credentials:**
   Ensure your AWS credentials are properly configured to allow the Boto3 library to interact with your AWS account.

2. **Run the Memory Monitoring Script:**
   ```
   ./memory_monitoring.sh
   ```
   This shell script will record available memory before and after clearing the cache and store the results in `available-memmory.txt`.

3. **Set Up Crontab:**
   Edit your crontab using `crontab -e` and add the following line to automate the script daily at 12:00 AM: 
   The first Command automate the script file 
   The second Command automate uploading the file to s3 Bucket 
   ```
   0 0 * * * /path/to/aws-memory-monitoring/memory_monitoring.sh

   0 0 * * * python3 ./home/kus/Documents/shell-scripting-projects/aws-s3-function.py

   ```

## Contributing:
We welcome contributions from the community. If you find issues or have suggestions for improvements, please feel free to open an issue or create a pull request.

## Contact:
For questions or feedback, please contact the project maintainer:
- Name: kushagra
- Email: kushagra746@example.com

## Acknowledgments:
We would like to thank the [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html?id) team for their excellent work on the AWS SDK for Python, which made this project possible.


