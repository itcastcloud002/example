# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'

#取内存总量
f = open('/proc/meminfo','r')

for lines in f:
    if lines.startswith("MemTotal:"):
        memtotal = int(lines.split()[1]) / 1024 /1024
    if lines.startswith("MemFree:"):
        memfree = int(lines.split()[1]) / 1024 / 1024
        break
print("Used:%.2fG - %.2fG = %.2fG" %(memtotal,memfree,memtotal - memfree))

