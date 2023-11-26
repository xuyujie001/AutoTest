"""
1。创建yaml文件
2.读取文件
3、输出文件
"""
import yaml
#打开文件  encoding="utf-8"
with open("./data.yml","r",encoding="utf-8") as f:
    #读取单个yaml文件
    #r = yaml.safe_load(f)
    #读取多个yaml文档
    r=yaml.safe_load_all(f)
    #循环输出文件内容
    for i in r:
        print(i)