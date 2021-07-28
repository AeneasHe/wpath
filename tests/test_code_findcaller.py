# -.- coding:utf-8 -.-
import wpath


@wpath.findcaller
def golden():
    return "metal"


@wpath.findcaller
def wood():
    return golden()


@wpath.findcaller
def water():
    return wood()


@wpath.findcaller
def fire():
    return water()


@wpath.findcaller
def land():
    return fire()


print(land())
