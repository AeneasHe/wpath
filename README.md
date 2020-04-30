# Gpath

help find the project root folder

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
add .env file to your project root folder.

## Useage

``` python
# this will add your root folder to python path
import gpath

# show project root folder
print(gpath.workspace)

```