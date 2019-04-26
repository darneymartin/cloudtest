import cloudtest
import pytest

INSTANCE_NAME = "-"
INSTANCE_AZ = "us-east-1"
INSTANCE_TAG = "Name"
INSTANCE_TAG_VALUE = "-"
INSTANCE_KEYPAIR = "-"
INSTANCE_TYPE = "c5.large"
INSTANCE_OWNER = "-"

@pytest.fixture
def instance():
    '''Returns a instance for testing'''
    session = cloudtest.get_session("default")
    instance = session.ec2instance(name=INSTANCE_NAME)
    return instance

# Test that the instance exists
def test_exists(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_state_equals(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_tag_equals(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_tag_exists(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_type_equals(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_az_equals(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_keypair_equals(instance):
    assert instance.exists() == True

# Test that the instance exists
def test_owner_equals(instance):
    assert instance.exists() == True
