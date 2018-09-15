# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'

s_file = '/usr/bin/ls' #源文件
d_file = '/home/sl' #目标文件

s_obj_file = open(s_file,'rb')

d_obj_file = open(d_file,'wb')
buffer_size = 4096

while True:
    data = s_obj_file.read(buffer_size)
    if not data:
        break
    d_obj_file.write(data)

s_obj_file.close()
d_obj_file.close()



