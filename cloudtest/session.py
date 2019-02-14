import cloudtest.backend.aws
import cloudtest.modules


class Session(object):

    def __init__(self, profile):
        self.profile = profile
        self.backend = cloudtest.backend.aws.AWS(self.profile)



    def __getattr__(self, name):
        #assert name in testinfra.modules.modules, name + " is not a module"
        module_class = cloudtest.modules.get_module_class(name)
        module_class.backend = self.backend
        #obj = module_class.get_module(self)
        obj = module_class
        #module_class()
        setattr(self, name, obj)
        return obj

def get_session(profile):
    session = Session(profile)
    return session
