from utils.RequestsUtil import Request
from config.Conf import ConfigYaml

url_path = ConfigYaml().get_conf_url()
#定义登录方法
def login():
    url = url_path +"/authorizations/"
    data = {"username":"python","password":"12345678"}

    request =Request()
    r = request.post(url,json=data)
    print(r)

def info():
    url = ""
    token = ""
    headers = {'Authorization': 'JWT' + token}

    request = Request()
    r = request.get(url,headers=headers)
    print(r)


def goods_list():
    url = ""
    data = {
        "page":"1",
        "page_size":"10",
        "ordering":"create_time"
    }

    request = Request()
    r = request.get(url, json=data)
    print(r)


def cart():
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


def order():
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
    login()
    #info()
    #goods_list()
    #cart()
    #order()