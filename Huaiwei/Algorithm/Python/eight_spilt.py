#!/usr/bin/python
# -*- coding: UTF-8 -*-

# •连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

def spilt_eight(str_input):
    results = []
    while str_input:
        str_input_len = len(str_input)
        if str_input_len < 8:
            result = str_input + '0' * (8 - str_input_len)
            str_input = ''
        else:
            result = str_input[:8]
            str_input = str_input[8:]
        results.append(result)
    return results

str1 = raw_input()
str2 = raw_input()
str1_results = spilt_eight(str1)
str2_results = spilt_eight(str2)
for str_result in str1_results + str2_results:
    print(str_result)
