#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 参考[[LeetCode]Evaluate Division ](http://bookshadow.com/weblog/2016/09/11/leetcode-evaluate-division/)
# 维基百科 [Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        # 如果没有设置字典key的value，默认为collections.defaultdict(int)
        g = collections.defaultdict(lambda: collections.defaultdict(int))
        for (s, t), v in zip(equations, values):
            g[s][t] = v
            g[t][s] = 1.0 / v
        # ford算法的核心就是不断搜索当前两个元素和其他元素的关系，如果有，利用其他元素更新当前元素即可
        for k in g:
            # 遍历字典的key，并设置对角线为1.0，也就是a/a=1.0
            g[k][k] = 1.0
            # 进行一次遍历行和列，如果a和b同时和c都有关系，那么更新a和b的值即可
            for s in g:
                for t in g:
                    if g[s][k] and g[k][t]:
                        g[s][t] = g[s][k] * g[k][t]
        ans = []
        for s, t in queries:
            ans.append(g[s][t] if g[s][t] else -1.0)
        return ans
