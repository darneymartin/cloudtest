from cloudtest.modules.base import Module

class S3Bucket(Module):
    """Test S3 Bucket Attributes"""

    def __init__(self, name):
        self.name = name
        super()

    def exists(self):
        """
        Method: exists
        Return: boolean based on the existance of a bucket
        """
        s3 = self.backend.session.resource('s3')
        exists = True
        try:
            s3.meta.client.head_bucket(Bucket=self.name)
        except Exception as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                exists = False
        return(exists)

    def tag_equals(self, key, value):
        """
        Method: tag_equals
        Return: boolean based on the value of a tag of a bucket
        """
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

    def tag_exists(self, key):
        """
        Method: tag_exists
        Return: boolean based on the existance of a tag of a bucket
        """
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

    def versioning_is_enabled(self):
        """
        Method: versioning_is_enabled
        Return: boolean based on the versioning of a bucket
        """
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

    def policy_status_equals(self, status):
        """
        Method: policy_status_equals
        Return: boolean based on the policy status of a bucket
        """
        pass

    def policy_equals(self, policy):
        """
        Method: policy_equals
        Return: boolean based on the policy of a bucket
        """
        pass

    def location_equals(self, location):
        """
        Method: location
        Return: boolean based on the location of a bucket
        """
        pass
