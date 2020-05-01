import os
import sys
import threading

class SingletonType(type):
    _instance_lock = threading.Lock()
    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType,cls).__call__(*args, **kwargs)
        return cls._instance




class Gpath(metaclass=SingletonType):
    def __init__(self):
        self.workspace=''
        self.flag=".env"
        self.find_gpath()

    def reset(self,flag):
        self.flag=flag
        self.workspace=self.find_gpath()
        return self.workspace

    def find_gpath(self,path=os.getcwd()):
        dirs = os.listdir(path)
        if self.flag in dirs:
            sys.path.append(path)
            return path
        else:
            if path=="/":
                self.workspace=None
                return None
                
            path=os.path.dirname(path)
            return self.find_gpath(path)

g = Gpath()
g.find_gpath()

def reset(flag=".env"):
    return g.reset(flag)

def workspace():
    return g.find_gpath()