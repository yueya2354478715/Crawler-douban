# -*- codeing =utf-8 -*-
# @Time:2020/12/7 18:34
# @Author:青
# @File:demo2.py
# @Software:PyCharm

# for循环
"""
for i in range(5):  # :代表下边的代码段属于它  0,1,2,3,4
    print(i)
"""
"""
for i in range(0, 10, 3):  # 从0开始，每次增长3
    print(i)
"""
"""
for i in range(-10,-100,-30):
    print(i)
"""
'''
name ="chengdu"  # 字符
for x in name:
    print(x,end='\t')
'''
'''
a = ["aa", "bb", "cc", "dd"]  # 列表
for i in range(len(a)):
    print(i, a[i])
'''

# while循环  递增变量
'''
i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i + 1))
    print("i=%d" % i)
    i += 1
'''

'''
# 1到100求和
n = 100
a_sum = 0
counter = 1
while counter <= n:
    a_sum = a_sum + counter
    counter += 1
print("1到%d的和为：%d" % (n, a_sum))

# b_sum = 0
# for i in range(1, 101):
#     b_sum = b_sum + i
# print("1到%d的和为：%d" % (i, b_sum))
'''
'''
count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:
    print(count, "大于或等于5")
'''

# break continue pass
'''
# break 结束整个循环
i = 0
while i < 10:
    i = i + 1
    print("-" * 30)
    if i == 5:
        break
    print(i)
'''
# continue 跳过当前循环，进入下一轮循环
'''
i = 0
while i < 10:
    i = i + 1
    print("-" * 30)
    if i == 5:
        continue  # 结束本次循环
    print(i)
'''
# pass 占位语句，没有实际意义