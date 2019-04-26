# cloudtest

cloudtest is a tool that can be used to test AWS cloud infrastructure.
It uses the boto3 module to handle the connections to AWS.

## Install
```bash
git clone https://github.com/darneymartin/cloudtest
cd cloudtest
python3 setup.py install
```
#### Setup AWS Profile
```bash
pip install awscli
aws configure
```

## Usage
```python
>>> import cloudtest
>>> session = cloudtest.get_session("default")
>>> bucket = session.s3bucket("bucket-name")
>>> bucket.exists()
>>> print str(bucket.exists())
True
>>> import cloudtest
>>> session = cloudtest.get_session("default")
>>> instance = session.ec2instance(name="instance-name")
>>> instance.exists()
>>> print str(instance.exists())
True
```

##### Upcoming Changes
* Refactoring to insure clear code
* Documentation on how to use
* Input Validation
* Addition of RDS and Route53 modules
* Build script to setup infrastructure for testing
