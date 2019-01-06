"""
为了避免当用户没有将python 装在默认的 /usr/bin 路径里，而找不到python解释器的问题。过程：
操作系统首先会到usr/bin/env里查找 python 的安装路径，
再调用对应路径下的解释器程序完成操作。这句代码的作用是让操作系统会去环境设置寻找python目录
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-


from sys import stdout

if __name__ == '__main__':
    A_VAR = int(input('输入四个数字:\n'))
    A_OUT = []
    A_OUT.append(A_VAR % 10)
    A_OUT.append(A_VAR % 100 / 10)
    A_OUT.append(A_VAR % 1000 / 100)
    A_OUT.append(A_VAR / 1000)

    for i in range(4):
        A_OUT[i] += 5
        A_OUT[i] %= 10
    for i in range(2):
        A_OUT[i], A_OUT[3 - i] = A_OUT[3 - i], A_OUT[i]
    for i in range(3, -1, -1):
        stdout.write(str(A_OUT[i]))
        