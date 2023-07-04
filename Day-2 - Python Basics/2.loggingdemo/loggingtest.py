import logging

#basic log configuration
logging.basicConfig(level=logging.DEBUG,format="%(asctime)s - %(levelname)s - %(message)s")

# logging variable value in debug level
a=5
logging.debug(f"The value of variable a is {a}")
logging.info("This is info level ")
logging.warning("This is in waring level")

#logging exception
try:
    1/0

except Exception as e:
    logging.error("Zero division error",exc_info=True)

#
logging.critical("This is critical level")


#custom logging
logger =logging.getLogger(__name__)


file_log=logging.FileHandler("custom_log.log")
formater1=logging.Formatter("%(levelname)s : %(name)s  :  %(message)s")
file_log.setFormatter(formater1)
logger.addHandler(file_log)

logger.info("This will save in file")

logger.warning("warning")
logger.critical("critical")


