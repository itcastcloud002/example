# _*_ coding:utf-8 _*_
__author__ = 'SmartGo'
"""size

包括加、减、乘、除
"""
#用于二位数加法运算
def jiafa(x,y):
    "Useage:jiafa(1,2)"
    return "%s + %s = %s" %(x,y,x + y)


#用于二位数减法运算
def jianfa(x,y):
    "Useage:jianfa(1,2)"
    return "%s - %s = %s" %(x,y,x - y)

#用于二位数乘法运算


#用于二位数除法运算

if __name__ == '__main__':
    print(jiafa(1,2))
    print(jianfa(9,3))