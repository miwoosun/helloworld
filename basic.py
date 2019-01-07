"""
为了避免当用户没有将python 装在默认的 /usr/bin 路径里，而找不到python解释器的问题。过程：
操作系统首先会到usr/bin/env里查找 python 的安装路径，
再调用对应路径下的解释器程序完成操作。这句代码的作用是让操作系统会去环境设置寻找python目录
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

 # operators 
if 5 > 2:
  print("Five is greater than two!")
x = 5
y = "John"
z = str(abs(x)) + y
print(x)
print(~x)
print(~2)
print(3**3)
print("the result is %s" %z)

# 字符串操作
sa = "Welcome! Are you completely new to programming? If not then we presume you will be looking for information about why and how to get started with Python.Fortunately an experienced programmer in any programming language (whatever it may be) can pick up Python very quickly. It is also easy for beginners to use and learn, so jump in!"

print("Enter your name:")
#x = input()
print("Hello, " + y)


thislist = list(("apple", "banana", "cherry"))
print(thislist)
print(thislist[1])
print(len(thislist))

for x in thislist:
  print(x)
that_fruit = "pear"
if that_fruit in thislist:
    print("Yes, %s is in the fruits list" %that_fruit)
else:
    print("No, %s is not in the fruits list" %that_fruit)

#thislist.clear()
print(thislist.count("apple"))


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)       