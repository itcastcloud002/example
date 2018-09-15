# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'

l1 = []
l1.append(int(input("first num:")))
l1.append(int(input("second num:")))

num = int(input("num:"))

for i in range(num-2):
    l1.append(l1[-1] + l1[-2])

print(l1)
