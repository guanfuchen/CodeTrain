#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串。（多组同时输入 ）
import sys
for input_str in sys.stdin:
    print(eval(input_str))
