# -*- codeing =utf-8 -*-
# @Time:2020/12/8 10:29
# @Author:青
# @File:demo5.py
# @Software:PyCharm

# 元组
# tuple 元组与list类似，不同之处在于tuple的元素不能修改。
# tuple写在小括号里，元素用逗号隔开
# 元组元素不可变，但可以包含可变对象，如list
'''
tupl = ()  # 创建空的元组 <class 'tuple'>
# tupl2 = (50)  # <class 'int'>
tupl2 = (50,)        # <class 'tuple'>
tup2 = (50, 60, 70)  # <class 'tuple'>
print(type(tupl), type(tupl2),type(tup2))
'''
'''
tup1 = ("abc", "def", 2000, 2020, 333, 444)
print(tup1[0])      # 访问第一个元素
print(tup1[-1])     # 访问最后一个元素
print(tup1[1:5])    # 左闭右开，进行切片
'''
# 增  连接
'''
tup1 = (12, 34, 56)
tup2 = ("abc", "def")
tup = tup1 + tup2
print(tup)
'''
# 删
'''
tup1 = (12, 34, 56)
print(tup1)
del tup1  # 删除了整个元组变量，从内存清空
print("删除后：", tup1)
'''
# 改
# tup1 = (12, 34, 56)
# tup1[0] = 100  # 报错，不允许修改

# 查
'''
tup1 = ("abc", "def", 2000, 2020, 333, 444)
print(tup1[0])
'''

# 字典 dict
# 字典是无序的对象集合，使用键值对(key-value)存储，具有极快的查找速度
# 键必须使用不可变类型
# 同一个字典中，键（key）必须是唯一的

info = {"name": "吴彦祖", "age": 18}  # 字典的定义

# 字典的访问
'''
print(info["name"])
print(info["age"])

# 访问了不存在的值
# print(info["gender"])          # KeyError: 'gender' 直接访问会报错
# print(info.get("gender"))      # 使用get方法没有找到对应的键，默认返回：None
print(info.get("age", "20"))  # 18
print(info.get("gender", "m"))  # 没找到，可以返回默认值
print(info.get("age", "20"))
'''

# 增
'''
info = {"name": "吴彦祖", "age": 18}
newID = input("请输入新的学号")
info["id"] = newID
print(info)
'''
# 删 del  clear
'''
info = {"name": "吴彦祖", "age": 18}
print("删除前：%s" % info["name"])
del info["name"]     
print("删除后：%s" % info["name"])   # 删除了指定整个键值对，再次访问会报错
'''
'''
# info = {"name": "吴彦祖", "age": 18}
# print("删除前：%s" % info)
# del info
# print("删除后：%s" % info)    # 删除字典后，再次访问会报错
'''
# 【clear】
# info = {"name": "吴彦祖", "age": 18}
# print("清空前：%s" % info)
# info.clear()
# print("清空后：%s" % info)    # 删除字典后，再次访问会报错

# 改
# info = {"name": "吴彦祖", "age": 18}
# info["age"]=20
# print(info["age"])

# 查
info = {"id": 1, "name": "吴彦祖", "age": 18}
# print(info.keys())   # 得到所有的键（列表） dict_keys(['id', 'name', 'age'])
# print(info.values()) # 得到所有的键（列表） dict_values([1, '吴彦祖', 18]
# print(info.items())  # 得到所有的项（列表），每个键值对是一个元组 dict_items([('id', 1), ('name', '吴彦祖'), ('age', 18)])

# 遍历所有的键
# for key in info.keys():
#     print(key)

# 遍历所有的值
# for value in info.values():
#     print(value)

# 遍历所有的键值对
# for key, value in info.items():
#     print("key=%s,value=%s" % (key, value))

# 使用枚举函数同时拿到列表中元素的下标和内容
mylist = ["a", "b", "c", "d"]
print(enumerate(mylist))
for i, x in enumerate(mylist):
    print(i, x)

# 集合set  去重
# set 和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中没有重复的key
# set无序的，重复元素在set中自动被过滤掉
