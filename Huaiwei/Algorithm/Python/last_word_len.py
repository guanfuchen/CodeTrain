#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 计算字符串最后一个单词的长度，单词以空格隔开。

input_str = raw_input()
last_word_len = len(input_str.split(' ')[-1])
print(last_word_len)