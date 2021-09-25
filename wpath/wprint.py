import platform

if platform.system()=="Windows":
    import colorama
    from colorama import init,Fore,Back,Style
    init(autoreset=True)
    
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


# format_print
def fprint(data):
    try:
        print(pretty(data))
    except:
        print("format error =========")


xprint = fprint

# color_print
def cformat(str_msg, mode=0, fg=None, bg=None):
    """
    显示方式: 0（默认）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
    前景色:   30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
    背景色:   40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）

    参考matlab的颜色缩写
    r 红 g 绿 b 蓝 y 黄 k 黑 w 白
    c 蓝绿 m 紫红
    """
    modes = [0, 1, 22, 4, 24, 5, 25, 7.27]
    fg_colors = [30, 31, 32, 33, 34, 35, 36, 37]
    bg_colors = [40, 41, 42, 43, 44, 45, 46, 47]

    colors = [
        "r",
        "red",
        "g",
        "green",
        "b",
        "blue",
        "y",
        "yellow",
        "k",
        "black",
        "w",
        "white",
        "m",
        "magenta",
        "c",
        "cyan",
    ]
    fg_color_map = {
        "r": 31,
        "red": 31,
        "g": 32,
        "green": 32,
        "b": 34,
        "blue": 34,
        "y": 33,
        "yellow": 33,
        "k": 30,
        "black": 30,
        "w": 37,
        "white": 37,
        "m": 35,
        "magenta": 35,
        "c": 36,
        "cyan": 36,
    }

    bg_color_map = {
        "r": 41,
        "red": 41,
        "g": 42,
        "green": 42,
        "b": 44,
        "blue": 44,
        "y": 43,
        "yellow": 43,
        "k": 40,
        "black": 40,
        "w": 47,
        "white": 47,
        "m": 45,
        "magenta": 45,
        "c": 46,
        "cyan": 46,
    }
    if mode in modes:
        pass
    elif int(mode) in modes:
        pass
    else:
        raise Exception("cprint: mode not true")

    if fg:
        if fg in colors:
            fg = fg_color_map[fg]
        elif fg in fg_colors:
            pass
        elif int(fg) in fg_colors:
            pass
        else:
            raise Exception("cprint: foreground color not true")
    if bg:
        if bg in colors:
            bg = bg_color_map[bg]
        elif bg in bg_colors:
            pass
        elif int(bg) in bg_colors:
            pass
        else:
            raise Exception("cprint: background color not true")

    color_template = f"{mode}"
    if fg:
        color_template += f";{fg}"
    if bg:
        color_template += f";{bg}"
    str_template = f"\033[{color_template}m{str_msg}\033[0m"
    return str_template


def cprint(str_msg, mode=0, fg=None, bg=None):
    print(cformat(str_msg, mode, fg, bg))


# log_format
def lformat(str_msg, level=None):
    level_map = {
        3: "error",
        "e": "error",
        2: "warning",
        "w": "warining",
        1: "success",
        "s": "success",
        0: "info",
        "i": "info",
        -1: "debug",
        "d": "debug",
    }
    if level in [3, 2, 1, 0, -1, "e", "w", "s", "i", "d"]:
        level = level_map[level]

    if level == "error":  # 3
        return cformat(str_msg, fg="r")
    elif level == "warning":  # 2
        return cformat(str_msg, fg="y")
    elif level == "success":  # 1
        return cformat(str_msg, fg="g")
    elif level == "info":  # 0
        return cformat(str_msg, fg="w")
    elif level == "debug":  # -1
        return cformat(str_msg, fg="b")
    else:
        return str_msg


def lprint(str_msg, level=None):
    print(lformat(str_msg, level))


def color_r(str_msg):
    return cformat(str_msg, fg="r")


def color_g(str_msg):
    return cformat(str_msg, fg="g")


def color_b(str_msg):
    return cformat(str_msg, fg="b")


def color_y(str_msg):
    return cformat(str_msg, fg="y")


def color_w(str_msg):
    return cformat(str_msg, fg="w")


def color_k(str_msg):
    return cformat(str_msg, fg="k")


def color_m(str_msg):
    return cformat(str_msg, fg="m")


def color_c(str_msg):
    return cformat(str_msg, fg="c")


def print_r(str_msg):
    return cprint(str_msg, fg="r")


def print_g(str_msg):
    return cprint(str_msg, fg="g")


def print_b(str_msg):
    return cprint(str_msg, fg="b")


def print_y(str_msg):
    return cprint(str_msg, fg="y")


def print_w(str_msg):
    return cprint(str_msg, fg="w")


def print_k(str_msg):
    return cprint(str_msg, fg="k")


def print_m(str_msg):
    return cprint(str_msg, fg="m")


def print_c(str_msg):
    return cprint(str_msg, fg="c")


if __name__ == "__main__":
    lprint("hello", level=1)
