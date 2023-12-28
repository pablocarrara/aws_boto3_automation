import boto3
from botocore.exceptions import ClientError


ec2 = boto3.client('ec2')


try:
    # Attempt to allocate an Elastic IP address for a VPC (Domain='vpc')
    allocation = ec2.allocate_address(Domain='vpc')

    # Associate the allocated Elastic IP address with an EC2 instance
    response = ec2.associate_address(
        AllocationId=allocation['AllocationId'],
        InstanceId='INSTANCE_ID'
    )

    # Print the response, which may contain information about the association
    print(response)

except ClientError as e:
    # Handle exceptions (e.g., if the allocation or association fails)
    print(e)



#A list called filters is created, which contains a dictionary specifying a filter for the describe_addresses method.
#In this case, it filters Elastic IP addresses based on the domain, and only those associated with a VPC are considered.
filters = [
    {'Name': 'domain', 'Values': ['vpc']}
]
response = ec2.describe_addresses(Filters=filters)
print(response)





#I request to the elastic ip address to be released using the AllocationId previously obtained when allocating
try:
    ec2.release_address(AllocationId = allocation['AllocationId'])
    print('Address released')
except ClientError as e:
    print(e)
