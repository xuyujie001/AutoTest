import  logging
#设置配置信息
logging.basicConfig(level=logging.INFO,format='%(asctime)s - %(filename)s - %(module)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
logger = logging.getLogger("log_demo")

logger.info("info")
logger.debug("debug")
logger.error("error")