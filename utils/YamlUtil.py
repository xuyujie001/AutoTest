#1。创建类
#2.初始化，文件是否存在
#3。yaml读取
import os.path

import yaml

#1。创建类
class YamlReader:
    # 2.初始化，文件是否存在
    def __init__(self, yamlfile):
        if os.path.exists(yamlfile):
            self.yamlfile= yamlfile
        else:
            raise FileNotFoundError("yaml文件不存在")
        self.__data = None
        self.__data_all = None

    # 3。yaml读取
    def data(self):#单文档读取
    #第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self.__data:
            with open(self.yamlfile,"rb") as f:
                self.__data=yaml.safe_load(f)
        return self.__data
    def data_all(self):#多文档读取
    #第一次调用data，读取yaml文档，如果不是，直接返回之前保存的数据
        if not self.__data_all:
            with open(self.yamlfile,"rb") as f:
                self.__data=yaml.safe_load_all(f)
        return  self.__data_all