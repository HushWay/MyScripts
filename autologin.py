#!/usr/bin/python3
# -*- coding: utf-8 -*-
import base64
import requests

#此处根据自己校园网Form Data中发送的数据进行更改
action = 'login'
username = '2019020374'
password = 'liuwei123'
ac_id = '1'
user_ip = '10.10.110.93'

# 登录地址
post_addr = "http://210.46.80.250:8008/portal/local/index.html"
# 构造头部信息 注意Cookie可能十分重要，而且Cookie会有过期时间（我们学校过期时间是1个月），过期之后，可能需要复制新的Cookie替换。
post_header = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
   'Accept': '*/*',
   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
   'Accept-Encoding': 'gzip, deflate',
   'Content-Type': 'application/x-www-form-urlencoded',
   'X-Requested-With': 'XMLHttpRequest',
   'Origin': 'http://210.46.80.250:8008',
   'Referer': 'http://210.46.80.250:8008/portal/local/index.html?uplcyid=null',
   'Content-Length': '86',
   'Cookie': 'logincookie={"username":"2019020374","loginipaddr":"10.10.110.93","logintime":"2021-10-12 10:38:25","secret":"ifedmirwveuronr","login_first_mod":"43201","unixlogintime":"1634006304","user_type":"0"}',
   'Host': '210.46.80.250:8008',
   'Connection': 'keep-alive',
}

post_data = {
   'action': action,
   'username': username,
   'password': password,
   'ac_id': ac_id,
   'user_ip': user_ip
}
# 发送post请求登录网页
z = requests.post(post_addr, data=post_data, headers=post_header)
# s = z.text.encode('utf8')
# print(s)
print("login success!")