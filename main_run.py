import os
import pytest

#调用pytest框架
if __name__ == '__main__':
    pytest.main(['-s',
                 '-v',
                 '--capture=sys',
                 '--clean-alluredir',
                 '--alluredir=allure-results'])#生成测试数据-用于生成html报告


#结合allure生成测试报告
os.system(r"allure generate -c -o reports")