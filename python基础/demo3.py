# -*- codeing =utf-8 -*-
# @Time:2020/12/7 19:17
# @Author:青
# @File:demo3.py
# @Software:PyCharm

# 字符串
# python源码文件默认以UTF-8编码，所以字符串都是unicode字符串

'''
word = "字符串"
sentence = "这是一个句子"
paragraph = """
    这是一个段落
    可以由多行组成"""
print(word)
print(sentence)
print(paragraph)
'''

# 单引号和双引号的区别
'''
my_str = "I'm a student" # '缩小
print(my_str)
my_str = 'I\'m a student'  # \转义
print(my_str)

# my_str = "Jason said \"I like you\""
my_str = 'Jason said "I like you"'  # 和上边一行实现结果一样
print(my_str)
'''
str = "chengdu" # 字符串当成列表来处理，截取字符串，拼接
'''
print(str)
print(str[0])
print(str[0:5])  # [起始位置：结束位置：步进值]
print(str[1:7:2])
print(str[:5])
print(str[5:])
print(str + "，你好")
print(str * 3)
'''


print(r"hello\nchengdu")  # 在字符串前面加r，表示直接显示原始字符串，不进行转义
# hello\nchengdu
print("hello\nchengdu")  # 使用反斜杠实现转义字符的功能
# hello
# chengdu