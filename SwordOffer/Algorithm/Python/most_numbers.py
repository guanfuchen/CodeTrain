#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 数组中有一个数字出现的次数超过数组长度的一半，
# 请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。
# 如果不存在则输出0。
# 使用系统的collections.Counter计数

import collections


class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        numbers_counter = collections.Counter(numbers)
        numbers_most = numbers_counter.most_common()[0]
        numbers_most_number = numbers_most[0]
        numbers_most_count = numbers_most[1]
        if numbers_most_count > len(numbers) / 2:
            return numbers_most_number
        else:
            return 0

if __name__ == '__main__':
    s = Solution()
    numbers = [1,2,3,2,2,2,5,4,2]
    print(s.MoreThanHalfNum_Solution(numbers))
