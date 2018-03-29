# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 22:35:23 2018

@author: peter
"""


def add(x, y):
    if len(x) > len(y):
        y = '0'*(len(x)-len(y))+y
    else:
        x = '0'*(len(y)-len(x))+x
    length = len(x)
    a = [0 for i in range(0, length+1)]
    carry = 0
    for i in range(0, length):
        temp = carry+int(x[length-i-1])+int(y[length-i-1])
        if temp >= 10:
            carry = 1
            temp = temp-10
        else:
            carry = 0
        a[length-i] = str(temp)
    if carry == 1:
        a[0] = '1'
    else:
        a[0] = ''
    return ''.join(a)


def sub(x, y):
    if len(x) > len(y):
        y = '0'*(len(x)-len(y))+y
    else:
        x = '0'*(len(y)-len(x))+x
    length = len(x)
    a = [0 for i in range(0, length)]
    lend = 0
    flag = 1
    for i in range(0, length):
        if x[i] == y[i]:
            continue
        if x[i] > y[i]:
            flag = 1
            break
        else:
            flag = 0
            x, y = y, x
            break
    for i in range(0, length):
        temp = lend+int(x[length-i-1])-int(y[length-i-1])
        if temp < 0:
            temp += 10
            lend = -1
        else:
            lend = 0
        a[length-i-1] = str(temp)
    while a[0] == '0':
        a.pop(0)
        if len(a)==0:
            return '0'
    if flag == 0:
        return '-'+''.join(a)
    else:
        return ''.join(a)


def mul(x, y):
    x = [int(x[i]) for i in range(len(x)-1, -1, -1)]
    y = [int(y[i]) for i in range(len(y)-1, -1, -1)]
    result = [0] * (len(x)+len(y))
    for i, j in enumerate(x):
        c = 0
        for k, l in enumerate(y):
            c, result[i+k] = divmod(j*l+c+result[i+k], 10)
        result[i+k+1] = c
    while result[-1] == 0:
        result.pop(-1)
    return ''.join([str(result[i]) for i in range(len(result)-1, -1, -1)])


def div(x, y):
    begin_y=y
    yushu = '0'
    shang = '1'
    if len(x) < len(y):
        return '0'
    elif len(x) == len(y):
        for i in range(1, 11):
            if sub(x, mul(y, str(i)))[0] == '-':
                i = i-1
                if i == 0:
                    return '0'
                shang = mul(shang, str(i))
                y = mul(y, str(i))
                yushu = sub(x, y)
                return shang
    else:
        shang = '1'+'0'*(len(x)-len(y)-1)
        if len(shang) > 1:
            y = y+shang[1:]
        for i in range(1, 101):
            if sub(x, mul(y, str(i)))[0] == '-':
                i = i-1
                shang = mul(shang, str(i))
                y = mul(y, str(i))
                yushu = sub(x, y)
                return add(shang, div(yushu, begin_y))


if __name__ == "__main__":
    while 1:
        try:
            x = input("请输入第一个正大数：")
            o = input("请输入运算符（支持+,-,*,/）：")
            if o not in'+-*/':
                raise Exception("请按提示输入！")
            y = input("请输入第二个正大数：")
            if o == '/' and y == '0':
                raise Exception("请输入正数！")
        except:
            print(("请按提示输入！"))
            continue
        else:
            break
    if o == '+':
        t = add(x, y)
    elif o == '-':
        t = sub(x, y)
    elif o == '*':
        t = mul(x, y)
    else:
        t = div(x, y)
    print(t)
    a=input("按任意键退出")
