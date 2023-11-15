import os
import boto3

#Generator function that returns all files in the directory starting with a given string
def list_to_upload(directory_path, starting_with_str):
    for f in os.listdir(directory_path):
        if os.path.isfile(f) and f.startswith(starting_with_str):
            yield f



# Create an S3 client
s3 = boto3.client('s3')



# directory containing the files to upload, bucket name where file will be uploaded, string variable used as condition
directory_path = '/home/pablo/my_ubuntu_python_apps'
bucket_name = 'mypyscriptsforjoa'
starting_with_str = 'joa'

#List all files in the directory starting with a given string
#files_to_upload = [f for f in os.listdir(directory_path) if os.path.isfile(f) and f.startswith(starting_with_str)]

#create the generator that returns all files in the directory starting with a given string
files_to_upload = list_to_upload(directory_path, starting_with_str)

#Upload each file to the S3 bucket
for file_name in files_to_upload:
    file_path = os.path.join(directory_path, file_name)
    s3.upload_file(file_path, bucket_name, file_name)
    print(f'Uploaded file {file_name} to {bucket_name}')



