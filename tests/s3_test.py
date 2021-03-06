import cloudtest
import pytest

@pytest.fixture
def bucket():
    '''Returns a bucket for testing'''
    session = cloudtest.get_session("default")
    bucket = session.s3bucket("bucket-name")
    return bucket

# Test that the bucket exists
def test_exists(bucket):
    assert bucket.exists() == True


def test_tag_exists(bucket):
    assert bucket.tag_exists("TestTag") == True
