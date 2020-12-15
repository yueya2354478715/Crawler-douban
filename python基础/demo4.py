# -*- codeing =utf-8 -*-
# @Time:2020/12/7 19:45
# @Author:青
# @File:demo4.py
# @Software:PyCharm

# 列表list
# 列表中元素类型可以不同，支持数字，字符串甚至是列表嵌套
# 列表索引值从0开始，-1为末尾的开始位置
# +拼接 *重复


'''
namelsit = []  # 空列表
namelsit = ["小张", "小李", "小王"]
print(namelsit[1])
print(namelsit[2])

testlist = [1, "测试"]  # 列表中可以存储混合类型
print(type(testlist[0]))
print(type(testlist[1]))
'''
# 遍历列表 使用循环
'''
namelist = ["小张", "小李", "小王"]
for name in namelist:
    print(name)

i = 0
while i < len(namelist):
    print(namelist[i])
    i = i+1
'''
namelist = ["小张", "小李", "小王"]
# 增加 append extend insert
'''
print("---增加前.名单列表的数据---")
for name in namelist:
    print(name)

nametemp = input("请输入添加学生的姓名：")
namelist.append(nametemp)  # 在末尾追加一个元素

print("---增加后.名单列表的数据---")
for name in namelist:
    print(name)
'''
a = [1, 2]
b = [3, 4]
a.append(b)  # 列表的嵌套，将列表当作一个元素
# print(a)
a.extend(b)  # 将b列表中每个元素逐一追加到列表中
# print(a)


a = [0, 1, 2]
a.insert(1, 3)  # 第一个表示下标，第二个表示元素（对象）
# print(a)        # 指定下标位置插入元素

# 删 [del]  [pop] [remove]
'''
movieName = ["加勒比海盗", "骇客帝国", "第一滴血", "指环王", "速度与激情", "指环王"]
print("---删除前.电影列表的数据---")
for name in movieName:
    print(name)

# del movieName[2]         # 指定下标位置删除一个元素
# movieName.pop()          # 弹出最后一个元素
movieName.remove("指环王")  # 直接删除指定内容的元素,只删除第一个
print("---删除后.电影列表的数据---")
for name in movieName:
    print(name)
'''

# 改
'''
print("---修改前.名单列表的数据---")
for name in namelist:
    print(name)

namelist[1] = "小陈"  # 修改指定下标的元素内容

print("---修改后.名单列表的数据---")
for name in namelist:
    print(name)
'''
# 查 【in ,not in】
'''
findName = input("请输入你要查找的学生姓名：")
if findName in namelist:
    print("在学员名单中找到了相同的名字")
else:
    print("没有找到")
'''

mylist = ["a", "b", "c", "a", "b"]
# print(mylist.index("a", 1, 4))  # 可以查找指定下标范围的元素，并返回找到数据的下标
# print(mylist.index("a", 1, 3))  # 范围区间，左闭右开[1,3) ,找不到会报错

# print(mylist.count("a"))  # 统计某个元素出现几次

# 排序
'''
a = [1, 4, 2, 3]
print(a)
# a.reverse()  # 将列表元素反转
# print(a)
a.sort()            # 默认将列表元素按升序序排列
print(a)
a.sort(reverse=True)  # 将列表元素按降序排列
print(a)
'''

schoolNmes = [[], [], []]  # 有3个元素的空列表，每个元素都是一个空列表
schoolNmes = [["北京大学", "清华大学"], ["天津大学", "南开大学", "中国民航大学"], ["山东大学", "中国改样大学"]]
# print(schoolNmes[0])
# print(schoolNmes[0][0])

# 8个老师随机分配到3个办公室

import random
offices = [[], [], []]
names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for name in names:
    index = random.randint(0, 2)  # 左闭右闭
    offices[index].append(name)

i = 1
for office in offices:
    print("办公室%d人数为%d" % (i, len(office)))
    i += 1
    for name in office:
        print("%s" % name, end='\t')
    print('\n')
    print("-"*20)

