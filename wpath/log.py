# 彩色日志模块

import logging


BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# The background is set with 40 plus the number of the color, and the foreground with 30

# These are the sequences need to get colored ouput
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"
BOLD_SEQ = "\033[1m"


def formatter_message(message, use_color=True):
    if use_color:
        message = message.replace("$RESET", RESET_SEQ).replace("$BOLD", BOLD_SEQ)
    else:
        message = message.replace("$RESET", "").replace("$BOLD", "")
    return message


COLORS = {
    "WARNING": YELLOW,
    "INFO": WHITE,
    "DEBUG": BLUE,
    "CRITICAL": YELLOW,
    "ERROR": RED,
}


class ColoredFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = (
                COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            )
            record.levelname = levelname_color
        return logging.Formatter.format(self, record)


# Custom logger class with multiple destinations
class ColoredLogger(logging.Logger):
    def __init__(self, name, min_length=None):
        logging.Logger.__init__(self, name, logging.DEBUG)

        if min_length:
            FORMAT = f"[$BOLD%(name)-{min_length}s$RESET][%(levelname)-20s]($BOLD%(pathname)s$RESET:%(lineno)d) : %(message)s "
        else:
            FORMAT = f"[$BOLD%(name)s$RESET] [%(levelname)-20s]($BOLD%(pathname)s$RESET:%(lineno)d) : %(message)s "

        COLOR_FORMAT = formatter_message(FORMAT, True)

        color_formatter = ColoredFormatter(COLOR_FORMAT)

        console = logging.StreamHandler()
        console.setFormatter(color_formatter)

        self.addHandler(console)
        return


if __name__ == "__main__":

    logging.setLoggerClass(ColoredLogger)
    color_log = logging.getLogger(__name__)
    color_log.setLevel(logging.DEBUG)

    color_log.debug("test")
    color_log.info("test")
    color_log.warning("test")
    color_log.error("test")
    color_log.critical("test")
