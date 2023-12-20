'''This script creates a new security group, associates it with a specified VPC, 
and sets inbound rules to allow traffic on ports 80 (HTTP) and 22 (SSH) from any IP address (0.0.0.0/0). 
The try-except block is used to catch any errors that may occur during the execution of the script.'''

import boto3
from botocore.exceptions import ClientError

# Create an EC2 client
ec2 = boto3.client('ec2')

# Describe VPCs (Virtual Private Clouds) to get the VPC ID
response = ec2.describe_vpcs()
vpc_id = response.get('Vpcs', [{}])[0].get('VpcId', '')

try:
    # Create a new security group within the specified VPC
    response = ec2.create_security_group(
        GroupName='SECURITY_GROUP_NAME',
        Description='DESCRIPTION',
        VpcId=vpc_id
    )
    
    # Extract the security group ID from the response
    security_group_id = response['GroupId']
    
    # Print a success message indicating the creation of the security group
    print('Security Group Created %s in VPC %s.' % (security_group_id, vpc_id))

    # Authorize inbound traffic for specific ports (HTTP and SSH in this case)
    data = ec2.authorize_security_group_ingress(
        GroupId=security_group_id,
        IpPermissions=[
            {'IpProtocol': 'tcp',
             'FromPort': 80,
             'ToPort': 80,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]},  # Allow all IP addresses for HTTP
            {'IpProtocol': 'tcp',
             'FromPort': 22,
             'ToPort': 22,
             'IpRanges': [{'CidrIp': '0.0.0.0/0'}]}   # Allow all IP addresses for SSH
        ]
    )
    
    # Print a success message indicating the setting of inbound rules
    print('Ingress Successfully Set %s' % data)

except ClientError as e:
    # Print any client errors that occur during the execution of the above code
    print(e)
