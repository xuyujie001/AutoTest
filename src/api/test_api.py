import requests
import pytest
import logging
import json
import allure
BASE_URL = "https://www.baidu.com"

def get_user(user_id, expected_name):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    #print("接口响应：",response.text)
    return response
    #assert response.status_code == 404
    #assert expected_name in response.json()["name"]

def create_user(user_data):
    response = requests.post(f"{BASE_URL}/users", json=user_data)
    #print("接口响应：",response.text)
    return response
    #assert response.status_code == 404
    #assert response.json()["id"] is not None