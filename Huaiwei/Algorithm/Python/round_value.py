#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

input_str  = raw_input()
print(int(round(eval(input_str))))
