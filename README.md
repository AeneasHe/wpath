# wpath

wpath: a package help add project workspace to python search path and other many small tools

python开发的一系列小工具,核心功能：

- 自动将当前项目的工作目录添加到python搜索包  
    工作目录的定义是：该目录下面有常见的项目级文件：.env,.gitignore,package.json,go.mod,go.sum,tsconfig.json
- 将某个目录添加到搜索目录  
    wpath.add("your folder path")
- 彩色 print  
    红：print_r，绿：print_r,蓝:print_b,黄：print_y,粉：print_m,黑:print_k,白:print_w
- 字典格式打印 print  
- 彩色日志处理模块 log  
- 时间处理模块 time  
- 代码调试模块 code  

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
