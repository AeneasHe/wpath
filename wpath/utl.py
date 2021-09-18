import datetime
import time
from print_pretty import print_pretty


def pretty(data, lpadding=1, not_end=False, max_len=0):
    if data == None:
        return "None"

    if type(data) == str:
        if len(data) > 50:
            data = data[:25] + "....." + data[-25:]
        return " " * lpadding + "'" + data + "'"

    if type(data) == int:
        return " " * lpadding + str(data)

    if type(data) == list:
        if len(data) > 9:
            join_split = ",\n"

            value = (
                "[\n"
                + join_split.join(
                    [pretty(d, lpadding=max_len + 5, not_end=False) for d in data]
                )
                + "\n"
                + " " * (max_len)
                + "\n]"
            )
            return value
        else:
            join_split = ","
            value = (
                "["
                + join_split.join(
                    [pretty(d, lpadding=max_len + 1, not_end=False) for d in data]
                )
                + " " * (max_len)
                + " ]"
            )
            return value

    if type(data) == dict:
        keys = data.keys()
        max_len = max([len(str(k)) for k in keys])
        values = "\n" + " " * lpadding + "{\n"
        for k in keys:
            if type(data[k]) == dict:
                value = pretty(data[k], lpadding=max_len + 5, not_end=True)

            elif type(data[k]) == list:
                value = (
                    "[\n"
                    + ""
                    + "\n".join(
                        [pretty(d, lpadding=max_len + 5, not_end=True) for d in data[k]]
                    )
                    + "\n"
                    + " " * (max_len + 3)
                    + "]"
                )
            else:
                # value = data[k]
                # if type(value) == str and len(value) > 50:
                #     value = value[:25] + "....." + value[-25:]
                value = pretty(data[k])

            value = str(value).lstrip("\n").lstrip(" ")

            values += (
                f'  {" "*lpadding}{"".ljust(max_len, " ")}{pretty(k)} : {value},\n'
            )

        values += " " * lpadding + "}"
        if not_end:
            values += ","
        return values


def yprint(data):
    if type(data) == dict:
        print_pretty(data)
    else:
        xprint(data)


if __name__ == "__main__":
    a = {"1": 2, 2: "a", 3: "b", 4: "c", 5: "d"}
    b = [
        a,
        a,
        a,
        a,
    ]
    xprint(b)
