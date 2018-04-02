#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，是的他们的和正好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        results = []
        mul_results = []
        for array_single_index, array_single in enumerate(array):
            result = None
            array_rest = tsum - array_single
            low = 0
            high = len(array)
            find_flag = False
            while low <= high:
                mid = (low+high)/2
                if array_rest == array[mid]:
                    if array_single_index != mid:
                        find_flag = True
                        result = [array_single, array[mid]]
                    break
                elif array_rest < array[mid]:
                    high = mid-1
                else:
                    low = mid+1
            if find_flag:
                results.append(result)
                mul_results.append(result[0]*result[1])

        # print(results)
        # print(mul_results)
        if results:
            return results[mul_results.index(min(mul_results))]
        else:
            return []

if __name__ == '__main__':
    s = Solution()
    # array = [1, 2, 3, 4, 5, 6, 7]
    # tsum = 8
    array = [1,2,4,7,11,16]
    tsum = 10
    print(s.FindNumbersWithSum(array, tsum))
