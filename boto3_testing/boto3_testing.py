import boto3, pprint

ec2_client = boto3.client('ec2')

regions = []

for region in ec2_client.describe_regions()['Regions']:
	regions.append(region['RegionName'])


for region in regions:
	ec2 = boto3.resource('ec2')
	print('Region: ', region)

	instances = ec2.instances.filter(
		Filters = [
		{'Name': 'instance-state-name',
		'Values': ['running']
		}
			]
		)

	for instance in instances:
		instance.stop()
		print('Stopped instance: ', instance.id)