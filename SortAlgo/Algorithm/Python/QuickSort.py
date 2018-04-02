#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 快速排序的思路就是取一个基准数字，使得其左边小于该基准数字，右边大于该基准数字
def quicksort(array):
    array_len = len(array)
    if array_len<=1:
        return array
    # 获取array中的数据，不断pop取出一个数字作为基准数字，直至结束
    base = array.pop()
    print('base:', base)
    less_array = []
    greater_array = []
    for array_data in array:
        if array_data <= base:
            less_array.append(array_data)
        else:
            greater_array.append(array_data)
    return quicksort(less_array)+[base]+quicksort(greater_array)



if __name__ == '__main__':
    array = [1, 5, 4, 3, 2, 6, 9, 8]
    array_sort = quicksort(array)
    print('array_sort:', array_sort)
    # print('array:', array)
    pass
