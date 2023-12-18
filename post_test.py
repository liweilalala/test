# -*- coding: utf-8 -*-
"""
@File ：post_test.py
"""
import requests
import json

if __name__ == '__main__':
    header = {
        "Host": "test-hello.test1.example.com"
    }
    # 发送json
    post_json = json.dumps({'some': 'data'})
    r1 = requests.post("http://10.99.192.72/postTest", data=post_json, headers=header)
    print("r1返回的内容为-->" + r1.text)
