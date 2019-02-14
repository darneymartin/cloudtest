import importlib

modules = {
    's3bucket': 'S3Bucket',
    'ec2instance': 'EC2Instance'
}


def get_module_class(name):
    modname = name
    classname = modules[name]
    modname = '.'.join([__name__, modname])
    module = importlib.import_module(modname)
    return getattr(module, classname)
