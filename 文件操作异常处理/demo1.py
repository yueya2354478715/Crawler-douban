# -*- codeing =utf-8 -*-
# @Time:2020/12/8 19:06
# @Author:青
# @File:demo1.py
# @Software:PyCharm
# 文件，是把一些数据存放起来，可以让程序下次执行的时候直接使用，而不必重新制作一份，省时省力

# 文件的打开，关闭，读取，写入
'''
f = open("test.txt", "w")   # 打开文件，w模式（写模式）文件不存在就新建
f.write("Hello world,I am here!")  # 将字符串写入文件
f.close()                   # 关闭文件
'''
# r ,w ,rb,wb
# read方法，读取指定的字符，开始时定位在文件头部，每执行一次向后移动指定字符数
'''
f = open("test.txt", "r")
content = f.read(5)  # 从文件读取5个字符
print(content)
content = f.read(10)  # 从文件读取5个字符
print(content)
f.close()
'''

'''
f = open("test.txt", "r")
content = f.readlines()  # 一次性读取全部文件为列表，每行一个字符串元素
i = 1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
f.close()
'''
'''
f = open("test.txt", "r")
content = f.readline()  # 每次读取一行
print("1:%s" % content, end="")
content = f.readline()
print("2:%s" % content)
f.close()
'''
import os
# os.rename("test1.txt","test.txt")