from .print import *

basic_types = [
    "<class 'list'>",
    "<class 'tuple'>",
    "<class 'dict'>",
    "<class 'set'>",
    "<class 'str'>",
    "<class 'int'>",
    "<class 'bool'>",
    "<class 'float'>",
    "<class 'complex'>",
]


def is_basic_type(var, already_typed=False):
    if already_typed:
        t = var
    else:
        t = type(var)

    if str(t) in basic_types:
        return True
    else:
        return False


def is_function(var, already_typed=False):
    if already_typed:
        t = var
    else:
        t = type(var)
    s = str(t)
    if "function" in s or "method" in s:
        return True
    else:
        return False


def is_object(var, already_typed=False):
    if "object at" in str(var):
        return True


def is_class(var, already_typed=False):
    if already_typed:
        t = var
    else:
        t = type(var)

    s = str(t)
    if s.startswith("<class") and (s not in basic_types):
        return True
    else:
        return False


def cstr(var, already_typed=False):
    s = str(var)
    if is_basic_type(var, already_typed):
        if type(var) == str:
            return color_c('"' + s + '"')
        return color_c(s)

    elif is_function(var, already_typed):
        return color_y(s)

    elif is_object(var, already_typed):
        return color_b(s)

    elif is_class(var, already_typed):
        return color_g(s)

    else:
        return s
