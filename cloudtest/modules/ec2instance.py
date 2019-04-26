from cloudtest.modules.base import Module

class EC2Instance(Module):

    """ Test EC2 Instances """

    def __init__(self, name=None, id=None):
        super()
        ec2 = self.backend.session.client('ec2')
        self.name = name
        self.id = id
        if name is not None:
            self.instance = ec2.describe_instances(
            Filters=[
            {
                'Name': 'tag:Name',
                'Values': [name]
            }])
        elif id is not None:
            self.instance = ec2.describe_instances(InstanceIds=[self.id])
        else:
            print("ERROR")
            pass
            #This is where an error needs thrown

        if len(self.instance["Reservations"][0]["Instances"]) > 0:
            self.instance_data = self.instance["Reservations"][0]["Instances"][0]
        else:
            self.instance_data = None

    def exists(self):
        if self.instance_data is not None:
            return True
        else:
            return False

    def state_equals(self, state):
        if self.instance_data["State"]["Name"] == state:
            return True
        else:
            return False

    def tag_equals(self, key, value):
        check = list(filter(lambda x: (x["Key"] == key and x["Value"] == value), data["Tags"]))
        if len(check) > 0:
            return True
        else:
            return False

    def tag_exists(self, key):
        check = list(filter(lambda x: (x["Key"] == key), data["Tags"]))
        if len(check) > 0:
            return True
        else:
            return False

    def type_equals(self, type):
        if self.instance_data["InstanceType"]== type:
            return True
        else:
            return False

    def az_equals(self, az):
        if self.instance_data["AvailabilityZone"]== az:
            return True
        else:
            return False

    def keypair_equals(self, keypair):
        if self.instance_data["KeyName"]== keypair:
            return True
        else:
            return False

    def owner_equals(self, owner):
        if self.instance_data["OwnerId"]== owner:
            return True
        else:
            return False
