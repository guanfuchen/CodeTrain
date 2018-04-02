#!/usr/bin/python
# -*- coding: UTF-8 -*-

# HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
# 今天测试组开完会后,他又发话了:在古老的一维模式识别中,
# 常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
# 但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
# 例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
# 你会不会被他忽悠住？(子向量的长度至少是1)

# 该方法非常巧妙，使用动态规划的问题，其中有两个目标，一个是先前数组中的最大值，一个是先前数组中包含最后一个元素的最大值
# 那么下一个最大值为包含新增的最大值以及先前的最大值的最大值，其中包含最后一个元素的最大值为先前的最大值和当前值的最大值

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        max_sum = array[0]
        res_sum = array[0]
        array_len = len(array)
        for i in range(1, array_len):
            res_sum = max(res_sum+array[i], array[i])
            max_sum = max(max_sum, res_sum)
        return max_sum

if __name__ == '__main__':
    s = Solution()
    array = [6,-3,-2,7,-15,1,2,2]
    print(s.FindGreatestSumOfSubArray(array))