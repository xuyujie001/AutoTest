import os
from utils.YamlUtil import YamlReader
#获取当前项目的绝对路径
current = os.path.abspath(__file__)

BASE_DIR = os.path.dirname(os.path.dirname(current))
#print(BASE_DIR)
#定义config目录的路径
_config_path= BASE_DIR + os.sep + "config"
#定义config.yaml文件的路径
_config_file= _config_path + os.sep + "conf.yaml"
#定义logs文件的路径
_log_path= BASE_DIR + os.sep + "logs/"
def get_config_path():
    return _config_path

def get_config_file():
    return _config_file

def get_log_path():
    #获取log文件路径
    return  _log_path
class ConfigYaml:
    def __init__(self):#初始化yaml读取配置文件
        self.config = YamlReader(get_config_file()).data()

    def get_conf_url(self):#定义方法获取需要信息
        return self.config["BASE"]["test"]["url"]

    def get_conf_log_level(self):
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]



if __name__ == '__main__':
    conf_read= ConfigYaml()
    print(conf_read.get_conf_url())
    print(conf_read.get_conf_log_level())
    print(conf_read.get_conf_log_extension())