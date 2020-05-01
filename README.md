# wpath

wpath: a package help you find the project workspace

## Install
```
git clone https://github.com/cofepy/wpath
cd wpath
python setup.py install
```
or
```
pip install wpath
```
## Env file
add .env file to your project workspace.

## Useage

``` python
import wpath
# this will add your workspace to python path
# by default, wpath will search parent folder which has an '.env' file as workspace flag

# show project workspace, 
# if not found the flag, wpath.workspace() will return None
print(wpath.workspace())

# change default flag
wpath.reset('.gitignore')
print(wpath.workspace())

```