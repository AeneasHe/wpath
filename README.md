# wpath

wpath: a package help add project workspace to python search path and other many small tools

python������һϵ��С����,���Ĺ��ܣ�

- �Զ�����ǰ��Ŀ�Ĺ���Ŀ¼��ӵ�python������  
    ����Ŀ¼�Ķ����ǣ���Ŀ¼�����г�������Ŀ���ļ���.env,.gitignore,package.json,go.mod,go.sum,tsconfig.json
- ��ĳ��Ŀ¼��ӵ�����Ŀ¼  
    wpath.add("your folder path")
- ��ɫ print  
    �죺print_r���̣�print_r,��:print_b,�ƣ�print_y,�ۣ�print_m,��:print_k,��:print_w
- �ֵ��ʽ��ӡ print  
- ��ɫ��־����ģ�� log  
- ʱ�䴦��ģ�� time  
- �������ģ�� code  

## Install

```bash
git clone https://github.com/aeneashe/wpath
cd wpath
python setup.py install
```

or

```bash
pip install wpath
```

## Env file

add one of flags [".env",".gitignore",".git","package.json"]  into your project workspace.

## Useage

- auto detect workspace folder  

``` python
import wpath
```

- show workspace folder

``` python
import wpath
# this will add your workspace to python path
# by default, wpath will search parent folder which has an '.env' file as workspace flag

# show project workspace, 
# if not found the flag, wpath.workspace() will return None
print(wpath.workspace())
```

- use your own flag as project folder root flag  

``` python
import wpath
# change default flag
wpath.reset(['.gitignore'])
print(wpath.workspace())

```

- color print

``` python
from wpath import print_r,print_g,print_b

print_r("red txt")
print_g("green txt")
print_b("blue txt")
```

- time tool

``` python
from wpath import today,now,yesterday

print(today())
print(now())
print(yesterday())
```

- log tool

```python
    from wpath import ColoredLogger
    logging.setLoggerClass(ColoredLogger)
    
    # use file name as logname, you can use any str as logname
    # logname=__file__  
    # logname=__name__
    # logname="module"

    logname="test log"

    log = logging.getLogger(logname)
    log.setLevel(logging.DEBUG)

    log.debug("test debug")
    log.info("test info")
    log.warning("test warning")
    log.error("test error")
    log.critical("test critical")

```
