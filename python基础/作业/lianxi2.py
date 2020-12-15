# -*- codeing =utf-8 -*-
# @Time:2020/12/7 19:06
# @Author:青
# @File:lianxi2.py
# @Software:PyCharm
# 九九乘法表
print("for循环实现九九乘法表")
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end="\t")
    print("\n")

print("while循环实现九九乘法表")
i = 1
while i < 10:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (i, j, i * j), end="\t")
        j = j+1
    print("\n")
    i = i + 1
