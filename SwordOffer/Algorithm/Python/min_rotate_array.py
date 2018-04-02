#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 把一个数组最开始的若干个元素搬到数组的末尾，
# 我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，
# 输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的
# 一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
# 使用旋转数组的特性，分为两个有序数组，最小值一定在另一个数组的第一个元素

class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        low = 0
        high = len(rotateArray) - 1

        while low < high:
            mid = (low + high) / 2
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            elif rotateArray[mid] == rotateArray[high]:
                high = high - 1
            else:
                high = mid
        return rotateArray[low]

