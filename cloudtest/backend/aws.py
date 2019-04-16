import boto3

class AWS(object):
    """AWS object that creates session to boto3"""

    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.session = boto3.Session(profile_name=self.profile_name)
