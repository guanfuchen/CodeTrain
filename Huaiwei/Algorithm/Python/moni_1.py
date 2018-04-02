#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

try:
    while True:
        input_str = sys.stdin.readline().strip()
        if input_str == '':
            break
        input_str = input_str.split()
        a = int(input_str[0])
        b = int(input_str[1])
        c = a + b
        print(c)
except:
    pass
