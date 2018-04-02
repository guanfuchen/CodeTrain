#!/usr/bin/python
# -*- coding:utf-8 -*-

# 递归方法
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         if n==0 or n==1:
#             return 1
#         else:
#             return self.Fibonacci(n-2)+self.Fibonacci(n-1)

# 动态规划方法
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n==0:
            return 0
        elif n==1 or n==2:
            return 1
        else:
            s = []
            s.append(1)
            s.append(1)
            for i in range(2, n):
                s.append(s[i-2]+s[i-1])
            return s[-1]

if __name__ == '__main__':
    s = Solution()
    for n in range(39):
        print(s.Fibonacci(n))
