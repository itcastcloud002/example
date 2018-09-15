# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'

import getpass
username = input("name:")

password = getpass.getpass("password:")
sb = 0
while True:
       if username == 'tom' and password == '123':
           print("登录成功")
           break
       else:
           sb = sb + 1
           print("登录失败%s次" %sb )

       username = input("name:")
       password = input("password:")

       if sb == 2:
            print("登录失败")
            break
