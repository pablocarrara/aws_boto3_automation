import boto3



#Command to use to access via ssh my ec2 instance after executing this script
#ssh -i path/to/id_rsa.pem ec2-user@your-instance-ip
#-i parameter indicates where the private key is saved


import boto3  # AWS SDK for Python
import os  # Operating system module for file system operations



ec2 = boto3.client('ec2')   # Create a client for interacting with Amazon EC2 services
key_pair_name = 'access_pablinca_toy_servers'   # Set the desired name for the new key pair
response = ec2.create_key_pair(KeyName = key_pair_name) # Request AWS to create a new key pair
private_key_path = 'id_rsa.pem' # Define the local file path to save the private key

with open(private_key_path, 'w') as key_file: # Open a file in write mode
    key_file.write(response['KeyMaterial']) # Write the private key material to the file

os.chmod(private_key_path, 0o400)  # Set correct permissions (read-only for the owner) for the private key file

print(f"Key pair '{key_pair_name}' created. Private key saved to {private_key_path}.")  # Print a confirmation message


# This code essentially fetches information about existing key pairs in your AWS account and prints the details,
# including key pair names and metadata. It's a simple way to view key pair information using the Boto3 library.

response = ec2.describe_key_pairs()
print(response)
