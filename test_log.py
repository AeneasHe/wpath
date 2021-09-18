from wpath import ColoredLogger
import logging

logging.setLoggerClass(ColoredLogger)
log = logging.getLogger("log")
log.setLevel(logging.DEBUG)

log.debug("test debug")
log.info("test info")
log.warning("test warning")
log.error("test error")
log.critical("test critical")