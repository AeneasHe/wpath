import os
import sys
import threading


class SingletonType(type):
    _instance_lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            with SingletonType._instance_lock:
                if not hasattr(cls, "_instance"):
                    cls._instance = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instance


FLAGS = [
    ".env",
    ".gitignore",
    ".git",
    "package.json",
    "go.mod",
    "go.sum",
    "tsconfig.json",
]


class Wpath(metaclass=SingletonType):
    def __init__(self):
        self.workspace = ""
        self.flags = FLAGS
        self.find_gpath()

    def reset(self, flags):
        self.flags = flags
        self.workspace = self.find_gpath()
        return self.workspace

    def find_gpath(self, path=os.getcwd()):
        dirs = os.listdir(path)
        for flag in self.flags:
            if flag in dirs:
                sys.path.insert(0, path)
                return path

        if path == "/" or ":" in path:
            self.workspace = None
            return None

        path = os.path.dirname(path)
        return self.find_gpath(path)


_wpath = Wpath()
_workspace = _wpath.find_gpath()

if not _workspace:
    raise Exception(
        f"No flag file: {FLAGS} is founded in project root folder.\n\
        Make sure your are in the project folder and add one flag file in it."
    )


def reset(flags=FLAGS):
    return _wpath.reset(flags)


def workspace():
    return _wpath.find_gpath()


def add(path):
    if os.path.exists(path):
        sys.path.insert(0, path)
    else:
        raise Exception(f"{path} not exists")