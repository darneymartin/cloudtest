# cloudtest

cloudtest is a tool that can be used to test AWS cloud infrastructure.
It uses the boto3 module to handle the connections to AWS.

## Install
```bash
pip3 install cloudtest
```
OR
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
```
