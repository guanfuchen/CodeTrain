#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
# 使得所有的奇数位于数组的前半部分，
# 所有的偶数位于位于数组的后半部分，
# 并保证奇数和奇数，偶数和偶数之间的相对位置不变。
# 类似于插入排序，不断满足奇数的条件

class Solution:
    def reOrderArray(self, array):
        # write code here
        array_len = len(array)
        for i in range(array_len):
            if array[i]%2==1:
                j = i-1
                while j>=0:
                    if array[j]%2==0:
                        # 交换j和j+1
                        array[j], array[j+1]=array[j+1], array[j]
                        j = j-1
                    else:
                        break
        return array

if __name__ == '__main__':
    array = [1,2,4,7,3,5,6,8]
    s = Solution()
    print(s.reOrderArray(array))
