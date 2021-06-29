import botocore
import boto3

#function to pull APPid
def get_instance_name(fid):
    # When given an instance ID as str e.g. 'i-1234567', return the instance 'Name' from the name tag.
    ec2 = boto3.resource('ec2')
    ec2instance = ec2.Instance(fid)
    instancename = ''
    for tags in ec2instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename


ec2 = boto3.resource('ec2', region_name='us-east-1')
#list out all volumnes 
#get all the tags associated with the ec2 
volumes = ec2.volumes.all()
instance = ec2.instances.all()
list_of_tags = []
AppId_list = []
for vol in volumes:
    print(vol)
    print('                                    ')
    print('********************************************')
    for inst in instance:
        print(inst.tags)
        list_of_tags.append(inst.tags)
        print(list_of_tags)
        for dic in list_of_tags:
            for tag in dic:
                if tag['Key'] == 'ApplicationId':
                    #AppId_list.append(tag['Key']
                    AppId_list.append(inst)
    print("THESE ARE THE APPIDS")
    print(AppId_list)
        # for tag in list_of_tags:
        #     if tag['Key'] == 'ApplicationId':
        #         AppId_list.append(tag['Value'])
        # if inst.tags.key == "ApplicationId":
        #     tagged = inst.tags.key.append
# print(tagged)
        

print('+++++++++++++++++++++++++++++++++++++++++++++')
print("THESE ONES ARE ATTACHED")
#list out only attached volumnes 
volumes = ec2.volumes.filter(Filters = [{
    'Name': 'status',
     'Values': ['in-use']
     }])

copable_tags_keys = ["ApplicationId"]

for vol in volumes:
    print(vol)
    print('                                    ')
    print('********************************************')
    for inst in instance:
        print(inst.tags)
        list_of_tags.append(inst.tags)
        print(list_of_tags)
        for dic in list_of_tags:
            for tag in dic:
                if tag['Key'] == 'ApplicationId':
                    #AppId_list.append(tag['Key'])
                    AppId_list.append(inst)
    print("THESE ARE THE APPIDS WHICH HAVE AN ATTACHED EC2")
    print(AppId_list)
   

client = boto3.client('ec2')

custom_filter = [{
    'Name': 'tag:Name'
}]
response = client.describe_instances(Filters = custom_filter)

