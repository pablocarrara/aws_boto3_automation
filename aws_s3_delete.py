from botocore.exceptions import ClientError


def delete_file(s3, bucket_name, file_name):
    obj = s3.Object(bucket_name, file_name)

    try:
        obj.load()
        obj.delete()
        print(f'the file {file_name} has been deleted from bucket {bucket_name}')
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            #Object does not exist
            print(f"The file {file_name} does not exist in {bucket_name}. No deletion performed.")
        else:
            #Other error, handle accordingly
            print(f'An error occurred: {e}')
