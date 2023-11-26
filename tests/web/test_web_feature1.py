import pytest

@pytest.fixture
def setup():
    # 可以在这里进行测试前的初始化工作
    yield
    # 可以在这里进行测试后的清理工作

def test_web_scenario1(setup):
    # 测试代码
    assert 1 == 1,"true"

def test_web_scenario2(setup):
    # 测试代码
    assert 1 == 2,"false"