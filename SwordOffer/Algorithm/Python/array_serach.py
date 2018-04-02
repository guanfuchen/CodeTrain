# -*- coding:utf-8 -*-
# 题目描述
# 在一个二维数组中，每一行都按照从左到右递增的顺序排序，
# 每一列都按照从上到下递增的顺序排序。请完成一个函数，
# 输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        array_len = len(array)
        for i in range(array_len):
            if target in array[i]:
                return 'true'
        return 'false'

# 针对异常的输入
while True:
    try:
        input_list = list(eval(raw_input()))
        target = input_list[0]
        array = input_list[1]
        S = Solution()
        print(S.Find(target, array))
    except:
        break
