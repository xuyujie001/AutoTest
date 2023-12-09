import pytest
from utils.RequestsUtil import Request
from config.Conf import ConfigYaml
from utils.AssertUtil import AssertUtil
url_path = ConfigYaml().get_conf_url()
from common.Base import init_db
#定义登录方法
def test_login():
    url = url_path +"/authorizations/"
    data = {"username": "python","password": "12345678"}
    request =Request()
    r = request.post(url,json=data)
    code = r["code"]
    body = r["body"]
    AssertUtil.assert_code(code,200)
    AssertUtil.assert_in_body(body,"")
    print(r)
    #1、初始化数据库对象
    conn = init_db("db_1")
    #2、查询结果
    res_db=conn.fetchone(sql="select id,username from tb_users where username='python")
    print("数据库查询结果：", res_db)
    #3、验证
    user_id = body["user_id"]
    assert user_id==res_db["id"]

def test_info():
    url = ""
    token = ""
    headers = {'Authorization': 'JWT' + token}

    request = Request()
    r = request.get(url,headers=headers)
    print(r)


def test_goods_list():
    url = ""
    data = {
        "page": "1",
        "page_size": "10",
        "ordering": "create_time"
    }
    request = Request()
    r = request.get(url, data=data)
    print(r)


def test_cart():
    url = ''
    data = {
        "sku_id": "3",
        "count": "1",
        "selected": "true"}
    token = ""
    headers = {'Authorization': 'JWT' + token}

    request =Request()
    r = request.post(url,json=data,headers=headers)
    print(r)


def test_order():
    url = ''
    data = {
        "sku_id": "3",
        "count": "1",
        "selected": "true"}
    token = ""
    headers = {'Authorization': 'JWT' + token}

    request =Request()
    r = request.post(url,json=data,headers=headers)
    print(r)

if __name__ == '__main__':
    test_login()
