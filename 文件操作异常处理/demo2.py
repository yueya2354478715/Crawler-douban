# -*- codeing =utf-8 -*-
# @Time:2020/12/8 19:29
# @Author:青
# @File:demo2.py
# @Software:PyCharm

# 异常
'''
# 发生异常
print("---test--1---")
f = open("123.txt", "r")  # 用只读模式打开了一个不存在的文件，报错
print("---test--2---")    # 这句代码不执行
'''

# 捕获异常
'''
try:
    print("---test--1---")
    f = open("123.txt", "r")
    print("---test--2---")
except IOError:  # 文件没找到属于IO异常（输入输出异常）
    pass         # 捕获异常后，执行的代码
'''
'''
try:
    print(num)
except NameError:  # 异常类型错误想要捕获，需要一致
    print("产生错误")
'''
'''
try:
    print("---test--1---")
    f = open("123.txt", "r")
    print("---test--2---")
    print(num)
except (NameError, IOError) as result:  # 将所有可能产生的异常类型，都放到下面的小括号里
    print("产生错误")
    print(result)
'''

# 捕获所有异常
'''
try:
    print("---test--1---")
    f = open("test.txt", "r")
    print("---test--2---")
    print(num)
except Exception as result:  # Exception可以承接任何异常
    print("产生错误")
    print(result)
'''

# try  finally 嵌套
import time
try:
    f = open("test.txt", "r")
    try:
        while True:
            content = f.readline()
            if len(content)==0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常...")
