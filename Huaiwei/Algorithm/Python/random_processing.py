#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
while True:
    try:
        num=input()
        num_list=[]
        for i in range(num):
            input_num=sys.stdin.readline()
            num_list.append(int(input_num[:-1]))
        num_list=sorted(list(set(num_list)))
        for i in num_list:
            print i
    except:
        break

