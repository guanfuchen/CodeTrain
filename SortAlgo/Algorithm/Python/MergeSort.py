#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 归并排序的思路是不断分解数组，然后将子数组排序合并，也就是分解合并
def mergesort(array):
    array_len = len(array)
    if array_len<=1:
        return array
    mid = array_len//2
    left = mergesort(array[0:mid])
    right = mergesort(array[mid:])
    return merge(left, right)

# 合并的思路是从头开始取最小的放入第三个数组中
def merge(left, right):
    left_len = len(left)
    right_len = len(right)
    left_index = 0
    right_index = 0
    result = []
    while left_index < left_len and right_index < right_len:
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # 最后较短的数据增加到末尾，最后的是array所以用+而不是append一个数据
    result+=left[left_index:]
    result+=right[right_index:]
    return result


if __name__ == '__main__':
    array = [1, 5, 4, 3, 2, 6, 9, 8]
    array_sort = mergesort(array)
    print('array_sort:', array_sort)
    pass
