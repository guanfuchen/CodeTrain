#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 插入排序就是不断插入到以排序好的序列中
def insertsort(array):
    array_len = len(array)
    for i in range(array_len):
        for j in range(i+1, 0, -1):
            if array[j] < array[j-1]:
                temp = array[j]
                array[j] = array[j-1]
                array[j-1] = temp
            else:
                break



if __name__ == '__main__':
    array = [1, 5, 4, 3, 2, 6, 9, 8]
    insertsort(array)
    print('array:', array)
    pass
