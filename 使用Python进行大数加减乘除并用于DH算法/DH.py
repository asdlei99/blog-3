# -*- coding: utf-8 -*-
"""
Created on Wed Mar 28 11:03:17 2018

@author: peter
"""
import Large_number_arithmetic

p = '12026655772210679470465581609002525329245\
773732132014742758935511187863487919026457076252932048619706\
498126046597130520643092209728783224795661331197604583'
g = '800251142659642435182926709953165139044805415345\
2321185350746845306277585856673898048740413439442356860630765545\
600353049345324913056448174487017235828857'
A = '1'
B = '1'
s = '1'
t = '1'
if __name__ == "__main__":
    print('Alice\'s public key is', g)
    print('Bob\'s public key is ', p)
    a = input('请输入a的私钥(推荐23):')
    b = input('请输入b的私钥(推荐24):')
    print("请耐心等待")
    for i in range(int(a)):
        A = Large_number_arithmetic.mul(A, g)
    A = Large_number_arithmetic.sub(
        A, Large_number_arithmetic.mul(p, Large_number_arithmetic.div(A, p)))
    print("Alice send A", A)
    print()
    for i in range(int(b)):
        B = Large_number_arithmetic.mul(B, g)
    B = Large_number_arithmetic.sub(
        B, Large_number_arithmetic.mul(p, Large_number_arithmetic.div(B, p)))
    print("Bob send B", B)
    for i in range(int(a)):
        s = Large_number_arithmetic.mul(s, B)
    s = Large_number_arithmetic.sub(
        s, Large_number_arithmetic.mul(s, Large_number_arithmetic.div(s, p)))
    print("secert key is", s)
    t = input("按任意键退出")
