# -*- codeing =utf-8 -*-
# @Time:2020/12/13 18:33
# @Author:青
# @File:testre.py
# @Software:PyCharm


# 正则表达式:字符串模式（判断字符串是否符合一定的标准）
import re

# 创建模式对象
pat = re.compile("AA")  # "AA"时正则表达式，用来去验证其他的字符串

# re.search()
# m = pat.search("CBA")  # search字符串被校验的内容 m=None未匹配
#
# m = pat.search("ABCAA") # <re.Match object; span=(3, 5), match='AA'> 左闭右开
#
# m = pat.search("AABCAADDCCAAA") # search进行比对查找，只找第一对
# print(m)

m = re.search("asd", "Aasd")  # 前面的字符串是规则（模式），后边的字符串是被校验的对象
# print(m)

# re.findall()
# print(re.findall("a","ASDaDFGAa"))  # 前面的字符串是规则（正则表达式），后边的字符串是被校验的对象

# print(re.findall("[A-Z]","ASDaDFGAa"))  # ['A', 'S', 'D', 'D', 'F', 'G', 'A']
# print(re.findall("[A-Z]+", "ASDaDFGAa"))  # ['ASD', 'DFGA']

# re.sub 替换
# print(re.sub("a", "A", "abcdcasd"))  # 在第三个字符串中找到a,用A替换; AbcdcAsd

# 建议在正则表达式中,被比较的字符串前面加上r,不用担心转义字符的问题
# a = r"\aabd-\'"  # \aabd-\'
# a = "\aabd-\'"     # abd-'
# print(a)

