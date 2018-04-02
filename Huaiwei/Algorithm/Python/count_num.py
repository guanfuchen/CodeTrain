#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 编写一个函数，计算字符串中含有的不同字符的个数。字符在ACSII码范围内(0~127)。不在范围内的不作统计。

def count_chars(input_str):
    input_str_set = []
    for input_str_single in input_str:
        if input_str_single not in input_str_set:
            input_str_set.append(input_str_single)
    return len(input_str_set)

input_str = raw_input()
print(count_chars(input_str))
