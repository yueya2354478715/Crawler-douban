# -*- codeing =utf-8 -*-
# @Time:2020/12/7 10:26
# @Author:青
# @File:demo1.py
# @Software:PyCharm

import random
import keyword

# print(len(keyword.kwlist),keyword.kwlist)
# print("hello,world")
'''
# 格式化输出
age = 18
print("我今年 %d 岁" % age)
print("我的名字是 %s\n我的国籍是 %s" % ("moon", "中国"))
print("www", "baidu", "com", sep=".")
print("hello", end="")
print("world", end='\t')
print("python", end="\n")
print("end")
'''

'''
查看变量类型
type(变量名)
'''
# 输入
# password = input("请输入密码:")  # 获取的是字符串
# # print(type(password))
# print("您刚输入的密码是:", password)

# a = eval(input("please input password:"))  # 获取值，脱掉引号；或者int强制类型转换
# print("your password is %d" % a)

for i in range(10):
    a = random.randint(0,2)
    print(a)

