# -*- codeing =utf-8 -*-
# @Time:2020/12/8 9:01
# @Author:青
# @File:lianxi3.py
# @Software:PyCharm
# 列表

products = [["iphone", 6888], ["MacPro", 14800], ["小米", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]
print("------商品列表------")
i = 0
for product in products:
    print("%d\t%s\t%d" % (i, product[0], product[1]), end='\n')
    i += 1
print("------选购商品------")
print("1.购买某件商品，请输入其编号(0-5)\n2.退出请按q")
buy_product = []
while True:
    buy_id = input("请输入:")
    if buy_id == 'q':
        print("------购买清单------")
        print("编号 数量\t商品\t价格")
        buylist = []
        for buy in buy_product:
            if buy not in buylist:
                buylist.append(buy)
        sumprice = 0
        for buy in buylist:
            sumprice = buy[1] * buy_product.count(buy) + sumprice
            print("  %d\t  %d\t\t%s\t%d" % (products.index(buy), buy_product.count(buy), buy[0], buy[1]))
        print("共计%d元" % sumprice)
        break
    buy_product.append(products[int(buy_id)])
