"""
创建类和测试方法
创建数据
创建参数化
运行
"""
import pytest


class TestDemo1:
        data_list1=["xiaoming","xiaohong"]

        @pytest.mark.parametrize("name",data_list1)
        def test_a(self,name):
            print("test_a")
            print(name)

        data_list2= [("xiaoming","123"), ("xiaohong","567")]
        @pytest.mark.parametrize(("name","password"),data_list2)
        def test_b(self,name,password):
            print("test_b")
            print(name,password)
