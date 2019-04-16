from cloudtest.modules.base import Module

class EC2Instance(Module):

    """ Test EC2 Instances """

    def __init__(self, name=None, id=None):
        ec2 = session.client('ec2')
        if name is not None:
            self.name = name
        elif id is not None:
            self.id = id
        else:
            pass
            #This is where an error needs thrown

    def exists(self):
        pass

    def state_equals(self, state):
        pass

    def tag_equals(self, key, value):
        pass

    def tag_exists(self, key):
        pass

    def type_equals(self, type):
        pass

    def az_equals(self, az):
        pass

    def keypair_equals(self, keypair):
        pass

    def owner_equals(self, owner):
        pass

    def has_securitygroup(self,sg_id):
        pass
