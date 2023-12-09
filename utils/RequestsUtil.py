import requests
from utils.LogUtil import my_log
#创建封装GET方法
def requests_get(url,headers=None):
#2.发送get请求
    r = requests.get(url,headers=headers)
#3.获取结果响应内
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body =r.text
#4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
#、字典返回
    return res

#创建封装POST方法
def requests_post(url,headers=None,json=None):
#2.发送post请求
    r = requests.post(url,headers=headers,json=json)
#3.获取结果响应内
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body =r.text
#4、内容存到字典
    res = dict()
    res["code"] = code
    res["body"] = body
#、字典返回
    return res

#重构
#1、创建类
class Request:
#2、定义公共方法
    def __init__(self):
        self.log=my_log("Requests")
    def requests_api(self, url, data=None, json=None, headers=None, cookies=None, method="get"):
        if method == "get":
            self.log.debug("发送get请求")
            r = requests.get(url,data=data,json=json,headers=headers,cookies=cookies)
        elif method == "post":
            self.log.debug("发送post请求")
            r = requests.post(url,data=data,json=json,headers=headers,cookies=cookies)

        code=r.status_code
        try:
            body=r.json()
        except Exception as e:
            body=r.text
        res = dict()
        res["code"] = code
        res["body"] = body

        return res
#3.重构get/post方法
    #定义方法，定义参数，调用公共方法
    def get(self,url,**kwargs):
        return  self.requests_api(url, method="get", **kwargs)

    def post(self,url,**kwargs):
        return  self.requests_api(url, method="post", **kwargs)