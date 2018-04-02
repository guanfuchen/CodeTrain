#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符


def reverse_sentence(input_str):
    reverse_str = ' '.join(input_str.split(' ')[::-1])
    return reverse_str

input_str = raw_input()
print(reverse_sentence(input_str))

