#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 写出一个程序，接受一个有字母和数字以及空格组成的字符串，和一个字符，然后输出输入字符串中含有该字符的个数。不区分大小写。

str1 = raw_input()
str2 = raw_input()
str_count = str1.count(str2.lower()) + str1.count(str2.upper())
print(str_count)