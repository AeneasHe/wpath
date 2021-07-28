import datetime
import time


def today():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def yesterday():
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def now():
    return int(time.time())

