# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'
import sys

for i in range(10):
    if i == 3:
        continue
    if i == 5:
        pass
    if i == 8:
        sys.exit()
    print(i)
else:
    print("end")