from cloudtest.modules.base import Module



class S3Bucket(Module):

    """ Test S3 Bucket Attributes"""

    def __init__(self, name):
        self.name = name
        super()

    #Status - OK
    def exists(self):
        s3 = self.backend.session.resource('s3')
        exists = True
        try:
            s3.meta.client.head_bucket(Bucket=self.name)
        except Exception as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                exists = False
        return(exists)

    #Status - Not Implemented
    def tag_equals(self, key, value):
        s3 = self.backend.session.resource('s3')
        exists = False
        try:
            response = s3.meta.client.get_bucket_tagging(Bucket=self.name)
            for x in response["TagSet"]:
                if x["Key"] == key and x["Value"] == value:
                    exists = True
                    return(exists)
                else:
                    exists = False
        except Exception as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                exists = False
        return(exists)

        #Status - OK
    def tag_exists(self, key):
        s3 = self.backend.session.resource('s3')
        exists = False
        try:
            response = s3.meta.client.get_bucket_tagging(Bucket=self.name)
            for x in response["TagSet"]:
                if x["Key"] == key:
                    exists = True
                    return(exists)
                else:
                    exists = False
        except Exception as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                exists = False
        return(exists)

    #Status - Not Implemented
    def versioning_is_enabled(self):
        s3 = self.backend.session.resource('s3')
        enabled = False
        try:
            response = s3.meta.client.get_bucket_versioning(Bucket=self.name)
            if response["Status"] == "Enabled":
                enabled = True
                return(enabled)
            else:
                enabled = False
        except Exception as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                enabled = False
        return(enabled)

    #Status - Not Implemented
    def policy_status_equals(self, status):
        pass

    #Status - Not Implemented
    def policy_equals(self, policy):
        pass

    #Status - Not Implemented
    def location_equals(self, location):
        pass
