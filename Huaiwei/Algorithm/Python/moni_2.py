#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 长度为n的数组乱序存放着0至n-1. 现在只能进行0与其他数的交换，完成以下函数

data_len = 10
input_list = range(data_len)
import random
random.shuffle(input_list)
# print(input_list)

def swap_with_zero(input_list, n):
    zero_index = input_list.index(0)
    input_list[zero_index], input_list[n] = input_list[n], input_list[zero_index]

for i in range(data_len-1, -1, -1):
    # print(i)
    if input_list[i] == i:
        continue
    # 需要将input_list中的数据交换到对应的位置，不能直接将这个数据交换到input_list[i]上，首先将0交换到input_list[i]上，然后将0交换到当前，完成数据的交换
    # print('-------------------')
    # print(input_list)
    swap_with_zero(input_list, input_list[i])
    swap_with_zero(input_list, i)
    # print(input_list)
    # print('-------------------')

for i in range(data_len-1, -1, -1):
    # print(i)
    if input_list[i] == i:
        continue
    # 需要将input_list中的数据交换到对应的位置，不能直接将这个数据交换到input_list[i]上，首先将0交换到input_list[i]上，然后将0交换到当前，完成数据的交换
    # print('-------------------')
    # print(input_list)
    swap_with_zero(input_list, input_list[i])
    swap_with_zero(input_list, i)
    # print(input_list)
    # print('-------------------')

print(input_list)
