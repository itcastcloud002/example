# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'

l1 = [1,2]

for i in range(8):
    l1.append(l1[i] + l1[i+1])
print(l1)