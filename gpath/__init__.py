import os
import sys

def find_gpath(path=os.getcwd()):
    dirs = os.listdir(path)
    if '.env' in dirs:
        sys.path.append(path)
        return path
    else:
        path=os.path.dirname(path)
        return find_gpath(path)


workspace=find_gpath()
