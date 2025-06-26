import boto3
import os


bucket_name = "aliqaaim5"
file_path = r"C:\Users\muzah\OneDrive\Documents\python-ALI\backups\newbackup2025-06-21.tar.gz"
s3_key = os.path.basename(file_path)
s3 = boto3.client("s3")


s3.upload_file(file_path, bucket_name, s3_key)
print("backup successfully uploaded")
