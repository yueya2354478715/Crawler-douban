# -*- codeing =utf-8 -*-
# @Time:2020/12/8 19:55
# @Author:青
# @File:lianxi1.py
# @Software:PyCharm
import time
# 引用文件操作的相关知识，通过Python新建一个文件gushi.txt，选择一首诗写入文件中
def writeshiFile(a):
    f = open("gushi.txt", "w")
    f.write(a)
    f.close()

gushi = """
        静夜思
         李白
床前明月光，疑是地上霜。
举头望明月，低头思故乡"""

'''
writeshiFile(gushi)


'''
# 另写一个函数，读取指定文件gushi.txt,将内容复制到copy.txt,并在控制台输出“复制完毕“
def copyFile(a,b):
    try:
        f = open(a, "r")
        f1 = open(b, "w")
        try:
            while True:
                content = f.readline()
                f1.write(content)
                if len(content) == 0:
                    break
                time.sleep(2)
                print(content, end="")
        finally:
            f.close()
            f1.close()
            print("\n文件关闭")
    except Exception as result:
        print("发生异常...")
# 分别写两个函数，完成读文件和写文件的操作，尽可能完善代码，添加异常处理


copyFile("gushi.txt","copy.txt")