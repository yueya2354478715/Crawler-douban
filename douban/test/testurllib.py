# -*- codeing =utf-8 -*-
# @Time:2020/12/10 18:20
# @Author:青
# @File:testurllib.py
# @Software:PyCharm
import urllib.request

# 获取一个get请求
# response = urllib.request.urlopen("http://www.baidu.com")  #
# print(response.read().decode('utf-8'))  # 对获取到的网页源码进行utf-8解码

# 获取一个post请求
# http://httpbin.org/ 网址进行测试
# response = urllib.request.urlopen("http://httpbin.org/post")  # 不能直接访问 HTTP Error 405: METHOD NOT ALLOWED
import urllib.parse

# data = bytes((urllib.parse.urlencode({"hello":"world"})), encoding='utf-8')  # post方法必须使用二进制封装数据送进去
# response = urllib.request.urlopen("http://httpbin.org/post", data=data)  # 送表单数据进入，可以模拟用户登陆
# print(response.read().decode('utf-8'))

# 超时处理
# try:
#     response = urllib.request.urlopen("http://httpbin.org/get",timeout=0.01)
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as result:
#     print("time out")

# response = urllib.request.urlopen("http://baidu.com")  # 418的意思是被网站的反爬程序返回的
# print(response.getheader("Server"))  # 正常执行状态码
# print(response.getheaders())

# 解决反爬机制
# url = "http://httpbin.org/post"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
#                   "Chrome/87.0.4280.88 Safari/537.36"}
# data = bytes(urllib.parse.urlencode({"name": "eric"}), encoding="utf-8")
# req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

# 访问豆瓣
url = "http://douban.com"
headers = {  # 浏览器的用户代理信息
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.88 Safari/537.36"}
req = urllib.request.Request(url=url, headers=headers)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))