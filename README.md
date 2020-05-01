# Gpath

Gpath: a package help you find the project workspace

## Install
```
git clone https://github.com/cofepy/gpath
cd gpath
python setup.py install
```
or
```
pip install gpath
```
## Env file
add .env file to your project workspace.

## Useage

``` python
import gpath
# this will add your workspace to python path
# by default, gpath will search parent folder which has an '.env' file as workspace flag

# show project workspace, 
# if not found the flag, gpath.workspace() will return None
print(gpath.workspace())

# change default flag
gpath.reset('.gitignore')
print(gpath.workspace())

```