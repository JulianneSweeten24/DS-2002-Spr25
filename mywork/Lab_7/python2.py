import boto3
import requests

file_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/0/00/Roman_Empire_Trajan_117AD.png/500px-Roman_Empire_Trajan_117AD.png'
local_filename = 'roman_empire.png'

response = requests.get(file_url)
if response.status_code == 200:
    with open(local_filename, 'wb') as f:
        f.write(response.content)
    print(f" Downloaded file to {local_filename}")
else:
    print("Failed to download the file.")
    exit(1)

bucket_name = 'my-first-bucket-wws6wv'  
s3_key = local_filename

s3 = boto3.client('s3', region_name='us-east-1')

try:
    with open(local_filename, 'rb') as file_data:
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=file_data,
            ACL='private'
        )
    print(f" Uploaded '{s3_key}' to S3 bucket '{bucket_name}'")
except Exception as e:
    print(f" Upload failed: {e}")
    exit(2)

expires_in = 604800  

try:
    presigned_url = s3.generate_presigned_url(
        'get_object',
        Params={'Bucket': bucket_name, 'Key': s3_key},
        ExpiresIn=expires_in
    )
    print("Presigned URL (valid for 7 days):")
    print(presigned_url)
except Exception as e:
    print(f"Failed to generate presigned URL: {e}")
import boto3
import requests


