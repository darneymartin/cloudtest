#from aws-infra-test.backend import Backend
import boto3

class AWS(object):
    """docstring for ."""

    def __init__(self, profile_name):
        self.profile_name = profile_name
        self.session = boto3.Session(profile_name=self.profile_name)
