#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 选择排序相当于寻找到最小或最大的，然后交换到最后
def selectesort(array):
    array_len = len(array)
    for i in range(array_len):
        min = i
        for j in range(i+1, array_len):
            if array[j] < array[min]:
                min = j
        temp = array[i]
        array[i] = array[min]
        array[min] = temp


if __name__ == '__main__':
    array = [1, 5, 4, 3, 2, 6, 9, 8]
    selectesort(array)
    print('array:', array)
    pass
