#OUTPUT of this script if I were in sa-east-1 region
# ***REGIONS:
# us-east-1
# us-west-2
# eu-central-1
# sa-east-1
# ...

# REGION: sa-east-1
# ZONES:
#        sa-east-1a
#        sa-east-1b
#        sa-east-1c
#        ...



import boto3

# Create an EC2 client
ec2 = boto3.client(service_name='ec2')

# Retrieve and print all AWS regions/endpoints
response_regions = ec2.describe_regions()
print('***REGIONS:')
for region in response_regions['Regions']:
    print(region.get('RegionName'))

print()

# Retrieve and print availability zones for the region of the EC2 client
response_availability_zones = ec2.describe_availability_zones()
region_name = response_availability_zones['AvailabilityZones'][0]['RegionName']

# Print the selected region
print(f"REGION: {region_name}")

# Print the availability zones for the selected region
print('ZONES: ')
for zone in response_availability_zones['AvailabilityZones']:
    print('      ', zone['ZoneName'])