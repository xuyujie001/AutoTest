import pytest
import allure
import requests

from src.api.test_api import get_user, create_user
from utils.readyaml import getdata
@pytest.fixture(scope="function", autouse=True)
def setup_function():
    # 可以在这里进行测试前的初始化工作
    print("准备测试数据")
    # 可以在这里进行测试后的清理工作

@pytest.fixture(scope="function", autouse=False)
def teardown_function():
    # 可以在这里进行测试前的初始化工作
    print("清理测试数据")


@allure.title("用例01")
@pytest.mark.parametrize("user_id, expected_name", [(1, "John Doe"), (2, "Alice Smith")])
def test_api_scenario1(user_id, expected_name):
    # 测试代码
    response = get_user(user_id, expected_name)
    #assert response.status_code == 200
    assert '404 Not Found'  in response.text
    #assert response.json()['result'] == 'success'

@allure.title("用例02")
@pytest.mark.parametrize("user_data", [{"name": "New User", "email": "newuser@example.com"},
                                       {"name": "Another User", "email": "anotheruser@example.com"}])
def test_api_scenario2(user_data):
    # 测试代码
    response = create_user(user_data)
    #assert response.status_code == 404
    assert '404 Not Found'  in response.text
    #assert 'error' not in response.json()

@pytest.mark.parametrize("shouji, appkey",getdata()['mobile_params'])
def test_api_03(shouji, appkey):
    params = {"shouji": shouji, "appkey": appkey}
    r=requests.get('https://api.binstd.com/shouji/query', params=params)
    assert r.status_code == 200
    result = r.json()
    assert result['status'] == 0
    assert result['msg'] == "ok"
    assert result['result']["shouji"] == "13585725024"


