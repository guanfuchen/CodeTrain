#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        numbers.sort()
        min_numbers = min(numbers)
        if min_numbers > 0:
            return range(min_numbers, min_numbers + 5) == numbers


if __name__ == '__main__':
    s = Solution()
    numbers = [1,2,3,4,5]
    print(s.IsContinuous(numbers))
