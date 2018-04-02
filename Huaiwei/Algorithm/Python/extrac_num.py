#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。

input_str = raw_input()
input_str = input_str[::-1]
input_set = []
res = ''
for input_str_single in input_str:
    if input_str_single not in input_set:
        input_set.append(input_str_single)
        res += input_str_single
print(res)


# def add_10(a, b):
#     return 10 * a + b


# print(input_set)
# print(reduce(add_10, input_set[::-1]))

