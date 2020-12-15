# -*- codeing =utf-8 -*-
# @Time:2020/12/10 19:46
# @Author:青
# @File:testbs4.py
# @Software:PyCharm

'''
BeatifulSoup4将复杂的HTML转换成一个复杂的树形结构，每个节点都是Python对象，所有对象可以归纳为4种：
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''

from bs4 import BeautifulSoup
import re

file = open("./baidu.html", "rb")  # 二进制读取
html = file.read().decode('utf-8')
bs = BeautifulSoup(html, "html.parser")
# print(type(bs))         # bs4.BeautifulSoup
# print(type(bs.title))   # bs4.element.Tag
# print(bs.a)
# print(bs.head)

# 1.Tag 标签及内容；拿到它所找到的第一个内容
# print(bs.title.string)  # 百度一下，你就知道
# print(type(bs.title.string))  #  <class 'bs4.element.NavigableString'>

# 2.NavigableString 标签里的内容（字符串）

# print(bs.a.attrs)   # {'class': ['mnav'], 'href': 'http://news.baidu.com', 'name': 'tj_trnews'} 字典


# 3.BeautifulSoup 表示整个文档
# print(bs.name)  # [document]
# print(bs.attrs)   # {}
# print(bs)

# 4.Comment 注释是一个特色的NavigableString,输出的内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))   # <class 'bs4.element.Comment'>
# ----------------
# =========

# 文档的遍历  遍历文档树
# print(bs.head.contents[1])  # 列表，下标访问
# 更多内容搜索文档

# 文档的搜索
# (1) find_all()
# 字符串过滤：会查找与字符串完全匹配的内容
t_list = bs.find_all("a")
# print(t_list)

# 2.正则表达式搜索：使用search（）方法来匹配内容
t_list1 = bs.find_all(re.compile("a"))


# print(t_list1)

# 3.方法：传入一个函数（方法），根据函数的要求来搜索 (了解)
def name_is_exists(tag):
    return tag.has_attr("name")


t_list3 = bs.find_all(name_is_exists)
# for item in t_list3:
#     print(item)

# 4.kwargs 参数
t_list4 = bs.find_all(id="head")
# for item in t_list4:
#     print(item)

# t_list5 = bs.find_all(class_=True)
t_list5 = bs.find_all(href="http://news.baidu.com")
# for item in t_list5:
#     print(item)

# 5. text 参数

# t_list6 = bs.find_all(text="hao123")
# t_list6 = bs.find_all(text=["hao123", "地图", "贴吧"])
t_list6 =bs.find_all(text=re.compile("\d"))  # 应用字符表达式来查找包含特定文本的内容，标签里的字符串 \d表示包含数字
# for item in t_list6:
#     print(item)

# 6.limit 参数
t_list7 = bs.find_all("a",limit=3)
# for item in t_list7:
#     print(item)

# css选择器
# t_list8 = bs.select("title")  # 通过标签查找

# t_list8 = bs.select('.mnav')    # .类   .mnav类名  通过类名查找

# t_list8 = bs.select('#u1')  # 通过id查找

# t_list8 = bs.select('a[class="bri"]')  # 通过属性查找

t_list8 = bs.select("head > title")  # 通过子标签来查找
t_list8 = bs.select(".mnav ~ .bri")  # 通过标签的兄弟来查找
print(t_list8[0].get_text())  # 得到文本

# for item in t_list8:
#     print(item)
