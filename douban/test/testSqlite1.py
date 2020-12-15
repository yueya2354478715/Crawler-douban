# -*- codeing =utf-8 -*-
# @Time:2020/12/15 10:47
# @Author:青
# @File:testSqlite1.py
# @Software:PyCharm

import sqlite3

# 增删改查
# conn =sqlite3.connect("test.db")  # 打开或创建数据库文件
# print("opened database successfully")

conn =sqlite3.connect("test.db")  # 打开或创建数据库文件

print("成功打开数据库")
c =conn.cursor()  # 获取游标
sql =""
c.execute(sql)   # 执行sql语句
conn.commit()      # 提交数据库操作
conn.close()       # 关闭数据库连接
print("成功建表")
#

