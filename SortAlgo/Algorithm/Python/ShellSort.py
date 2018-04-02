#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 希尔排序的思路是，以一定步长分割序列为一定子序列，然后对组成的一列进行排序
def shellsort(array):
    array_len = len(array)
    gap = array_len//2
    while gap > 0:
        # 对gap的这些元素进行直接插入
        # print('gap:', gap)
        # 遍历所有待插入的序列
        for i in range(gap, array_len, 1):
            # print('i:', i)
            # 对一列进行操作，原先分为(0,gap-1)和(gap,array_len-1)
            temp = array[i]
            j = i
            # 和先前的比，如果比先前的大，插入然后在比较
            while j >= gap and array[j - gap] > temp:  # 插入排序
                # print('j:', j)
                array[j] = array[j - gap]
                j = j - gap
            array[j] = temp
        gap = gap//2



if __name__ == '__main__':
    array = [1, 5, 4, 3, 2, 6, 9, 8]
    shellsort(array)
    print('array:', array)
    pass
