# -*- codeing =utf-8 -*-
# @Time:2020/12/8 18:39
# @Author:青
# @File:lianxi4.py
# @Software:PyCharm

# 函数
# 1.写一个打印一条横线的函数。
def printOneLine():
    print("-" * 30)


printOneLine()


# 2.写一个函数，可以通过输入的参数，打印出自定义行数的横线
def printNumLine(a):
    for i in range(a):
        printOneLine()


printNumLine(3)


# 3.写一个函数求三个数的和
def sum3Num(a, b, c):
    return a + b + c


result = sum3Num(1, 2, 3)
print("1+2+3=%d" % result)


# 4.写一个函数求三个数的平均值
def average3Num(a, b, c):
    sumResult = sum3Num(a, b, c)
    aveResult = sumResult / 3.0
    return aveResult
    # print("%d,%d,%d的平均值为%d" % (a, b, c, aveResult))


result = average3Num(5, 7, 9)
print("平均值为:", result)
print("平均值为:%d" % result)

# 全局变量 局部变量
a = 100


def test1():
    global a   # 声明全局变量的标识符
    print("test1--------修改前：a=%d" % a)
    a = 200
    print("test1--------修改后：a=%d" % a)


def test2():
    # a = 500  # 不同的函数可以定义相同的名字，彼此无关 ；局部变量
    print("test2--------修改前：a=%d" % a)


test1()
test2()

# 全局变量和局部变量名字相同，局部变量优先使用，没有局部变量，默认使用全局变量

# 在函数中修改全局变量
