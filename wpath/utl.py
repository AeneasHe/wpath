import datetime
import time


def today():
    return datetime.datetime.now().strftime("%Y-%m-%d")


def yesterday():
    return (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")


def now():
    return int(time.time())


def pretty(data, lpadding=1, not_end=False):
    if data == None:
        return "None"
    if type(data) == str:
        if len(data) > 50:
            data = data[:25] + "....." + data[-25:]
        return " " * lpadding + data

    if type(data) == list:
        value = (
            "[\n"
            + ""
            + "\n".join(
                [pretty(d, lpadding=max_len + 7, not_end=True) for d in data[k]]
            )
            + "\n"
            + " " * (max_len + 5)
            + "]"
        )
        return value

    keys = data.keys()
    max_len = max([len(k) for k in keys])
    values = " " * lpadding + "{\n"
    for k in keys:
        if type(data[k]) == dict:
            value = pretty(data[k], lpadding=max_len + 5, not_end=True)

        elif type(data[k]) == list:
            value = (
                "[\n"
                + ""
                + "\n".join(
                    [pretty(d, lpadding=max_len + 7, not_end=True) for d in data[k]]
                )
                + "\n"
                + " " * (max_len + 5)
                + "]"
            )
        else:
            value = data[k]
            if type(value) == str and len(value) > 50:
                value = value[:25] + "....." + value[-25:]
        value = str(value).lstrip("\n").lstrip(" ")
        values += f'  {" "*lpadding}{k.ljust(max_len, " ")} : {value},\n'

    values += " " * lpadding + "}"
    if not_end:
        values += ","
    return values


def xprint(data):
    try:
        print(pretty(data))
    except:
        print("format error =========")

