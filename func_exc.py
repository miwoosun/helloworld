"""
为了避免当用户没有将python 装在默认的 /usr/bin 路径里，而找不到python解释器的问题。过程：
操作系统首先会到usr/bin/env里查找 python 的安装路径，
再调用对应路径下的解释器程序完成操作。这句代码的作用是让操作系统会去环境设置寻找python目录
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

#def __fun_add__(int a, int b):
from sys import stdout

if __name__ == '__main__':
    A_VAR = 12 #int(input('输入四个数字:\n'))
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
    #  for i in range(3, -1, -1):
    #  stdout.write(str(A_OUT[i]))

def my_function(fname):
    print(fname + " Refsnes")
      
my_function("Emil")
my_function("Tobias")
my_function("Linus")

# 
def myfunc(n):
    return lambda a : a * n

mytripler = myfunc(3)
mytripler1 = myfunc(2)
print(mytripler(11))
print(mytripler1(11))

# Python Class/Object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
p1.myfunc()
p1.age = 12

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

import mymodule
mymodule.greeting("wumin")

a = mymodule.person1["age"]
print(a)

import platform
import datetime

x = platform.system()
print(platform.python_version())
#print(dir(datetime))


import json

# some JSON: dict list tuple str int float True Flase None null
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if (x):
    print("YES! We have a match!")
else:
    print("No match")
str = "The rain in Spain"
x = re.findall("ai", str)
print(x)