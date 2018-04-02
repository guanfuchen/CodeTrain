#!/usr/bin/python
# -*- coding: UTF-8 -*-


# 数据表记录包含表索引和数值，请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

import sys
import collections

table = {}

try:
    while True:
        table_num = int(sys.stdin.readline())
        for i in range(table_num):
            input_str = sys.stdin.readline().strip()
            if input_str == '':
                break
            input_str = input_str.split(' ')
            key_str = input_str[0]
            value = int(input_str[1])
            if key_str not in table:
                table[key_str] = value
            else:
                table[key_str] = table[key_str] + value
        table_order = collections.OrderedDict(sorted(table.items()))
        for k, v in table_order.items():
            print('{} {}'.format(k, v))
        break
except:
    pass
