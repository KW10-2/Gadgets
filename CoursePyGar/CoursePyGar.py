# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 21:13:04 2023

@author: lvjih
"""
import json
import time
import requests

#(paste and correct codes here)

while True:
    response = requests.post(
        'https://xk.nju.edu.cn/xsxkapp/sys/xsxkapp/elective/volunteer.do',
        cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    res = json.loads(response.text)
    code = res['code']
    localtime = time.asctime(time.localtime(time.time()))
    if code != "1":
        print(localtime, "失败！")
    if code == "1":
        print("成功！")
        break
    time.sleep(10)
        
        
        

