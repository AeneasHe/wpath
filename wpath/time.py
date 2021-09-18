import datetime
import time


def today():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def yesterday():
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def now():
    return int(time.time())


def ftime(t, format):
    return t.strftime(format)


def ptime(s, format):
    return datetime.datetime.strptime(s, format)

def dtime(t1,t2):
    # datetime.timedelta
    return t2-t1

if __name__ == "__main__":
    t = ptime("2021-01-05", "%Y-%m-%d")
    print(t)