# -*- codeing =utf-8 -*-
# @Time:2020/12/7 11:05
# @Author:青
# @File:lianxi1.py
# @Software:PyCharm

# 剪刀、石头、布游戏
import random
for i in range(20):
    a = eval(input("请输入剪刀（0）、石头（1）、布（2）："))
    if a not in [0, 1, 2]:  # 判断输入是否合法
        print("您的输入有误，请输入0-2")
        a = eval(input("请输入剪刀（0）、石头（1）、布（2）："))
    b = random.randint(0, 2)
    print("对手出了%d" % b)
    if a == b:
        print("平手")
    elif (a < b and abs(a-b) == 1) or (a > b and abs(a-b) == 2):
        print("你输了")
    else:
        print("你赢了")
