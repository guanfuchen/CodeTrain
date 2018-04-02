#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一个整数，将这个整数以字符串的形式逆序输出
# 程序不考虑负数的情况，若数字含有0，则逆序形式也含有0，如输入为100，则输出为001

def reverse_str(input_int):
    input_str = str(input_int)
    reverver_str = input_str[::-1]
    return reverver_str

input_int = int(raw_input())
print(reverse_str(input_int))

