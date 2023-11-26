#输出控制台
#1设置logger名称
#2设置log级别
#3创建handler
#4设置日志级别
#5定义输出格式
#6添加handler
#7运行输出
import logging
#1设置logger名称
logger = logging.getLogger("log_file_demo")
#2设置log级别
logger.setLevel(logging.INFO)
#3创建handler
fh_stream = logging.StreamHandler()
fh_file= logging.FileHandler("./test.log")
#4设置日志级别
fh_stream.setLevel(logging.DEBUG)
fh_file.setLevel(logging.WARNING)
#5\定义输出格式
formatter = logging.Formatter('%(asctime)s  %(filename)s %(module)s %(funcName)s %(lineno)d - %(levelname)s - %(message)s')
fh_stream.setFormatter(formatter)
fh_file.setFormatter(formatter)
#6添加handler
logger.addHandler(fh_stream)
logger.addHandler(fh_file)
#7运行输出
logger.info("这是一个info级别日志")
logger.debug("这是一个debug级别日志")
logger.warning("这是一个warning级别日志")