import boto3  # Import the Boto3 library for interacting with AWS services
import sys  # Import the sys module for accessing command-line arguments
from botocore.exceptions import ClientError  # Import the ClientError class for handling Boto3 errors
import json  # Import the json module for working with JSON data


def read_instance_ids(file_path):
    # A generator function that reads instance IDs from a JSON file
    with open(file_path, 'r') as file:
        data = json.load(file)
        instance_ids = data.get('instance_ids', [])
        for instance_id in instance_ids:
            yield instance_id


# Read command-line arguments
action = sys.argv[1]
instance_id = sys.argv[2]

# Create an EC2 client using Boto3
ec2 = boto3.client('ec2')

# Generate instance IDs from the specified JSON file
id_generator = read_instance_ids('instance_ids.json')

# Check the action specified in the command-line argument
if action == 'ON':
    # Dry run operation to verify permissions
    try:
        for instance_id in id_generator:
            ec2.start_instances(instanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        # Check if the error is due to DryRunOperation not being allowed
        if 'DryRunOperation' not in str(e):
            raise

    # Recreate the generator for the second try block
    id_generator = read_instance_ids('instance_ids.json')

    # Dry run succeeded, run start_instances without dry run
    try:
        for instance_id in id_generator:
            response = ec2.start_instances(InstanceIds=[instance_id], DryRun=False)
            print(response)
    except ClientError as e:
        print(e)

else:
    # Do a dry run operation to verify permissions
    try:
        for instance_id in id_generator:
            ec2.stop_instances(instanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        # Check if the error is due to DryRunOperation not being allowed
        if 'DryRunOperation' not in str(e):
            raise

    # Recreate the generator for the second try block
    id_generator = read_instance_ids('instance_ids.json')

    # Dry Run succeeded, call stop_instances without dry run
    try:
        for instance_id in id_generator:
            response = ec2.stop_instances(instanceIds=[instance_id], DryRun=False)
            print(response)
    except ClientError as e:
        print(e)
