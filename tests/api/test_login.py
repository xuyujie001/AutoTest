import pytest

from config import Conf
import os
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
from utils.YamlUtil import YamlReader

#获取测试用例内容list
#获取testlogin.yaml文件路径
test_file=os.path.join(Conf.get_data_path(),"testlogin.yaml")
#print(test_file)
#使用工具类来读取多个文档
data_list=YamlReader(test_file).data_all()
print(data_list)
#参数化执行测试用例
@pytest.mark.parametrize("login", data_list)
def test_yaml(login):
    url=ConfigYaml().get_conf_url()+login["url"]
    data=login["data"]
    request=Request()
    res=request.post(url,json=data)
    print(res)
#url,data,期望结果
if __name__ == '__main__':
    print(test_file)
    print(data_list)

