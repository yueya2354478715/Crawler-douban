# -*- codeing =utf-8 -*-
# @Time:2020/12/8 17:15
# @Author:青
# @File:demo6.py
# @Software:PyCharm

# 函数 代码复用

# 函数定义
def printinfo():  # 无参函数定义
    print("-" * 30)
    print("\t人生苦短，我用python")
    print("-" * 30)


# 函数调用
# printinfo()
# printinfo()


# 带参函数定义
def add2Num(a, b):
    c = a + b
    print(c)


# add2Num(11, 22)  # 函数调用


# 带返回值的函数
def add2Num1(b, c):
    return b + c


# a = add2Num1(11, 22)
# print(a)


# 返回多个值
def divid(a, b):
    shang = a // b
    yushu = a % b
    return shang, yushu  # 多个返回值用逗号分隔


# sh, yu = divid(5, 2)  # 需要使用多个值来保存返回内容
# print("商:%d,余数:%d " % (sh, yu))
