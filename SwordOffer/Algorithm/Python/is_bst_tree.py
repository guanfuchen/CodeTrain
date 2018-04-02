#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
# BST的后序序列的合法序列是，对于一个序列S，最后一个元素是x （也就是根），
# 如果去掉最后一个元素的序列为T，那么T满足：T可以分成两段，前一段（左子树）小于x，
# 后一段（右子树）大于x，且这两段（子树）都是合法的后序序列。完美的递归定义 : ) 。

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        sequence_len = len(sequence)
        if sequence_len == 0:
            return False
        if sequence_len == 1:
            return True
        root = sequence[-1]
        spilt_index = 0
        spilt_index_may = 0
        for i in range(sequence_len - 1):
            spilt_index_may = i
            if sequence[i] < root:
                pass
            else:
                break
        spilt_index_may += 1
        # print('spilt_index_may:', spilt_index_may)
        for j in range(spilt_index_may, sequence_len - 1):
            if sequence[j] < root:
                return False
        spilt_index = spilt_index_may
        # print('spilt_index_may:', spilt_index_may)
        # print('spilt_index:', spilt_index)
        left_sequence = sequence[:spilt_index]
        right_sequence = sequence[spilt_index:sequence_len - 1]
        left_is_bst = True
        right_is_bst = True
        # print('left_sequence:', left_sequence)
        # print('right_sequence:', right_sequence)
        if left_sequence:
            left_is_bst = self.VerifySquenceOfBST(left_sequence)
        if right_sequence:
            right_is_bst = self.VerifySquenceOfBST(right_sequence)
        # print('left_is_bst:', left_is_bst)
        # print('right_is_bst:', right_is_bst)
        return left_is_bst and right_is_bst

if __name__ == '__main__':
    s = Solution()
    sequence = [4,6,7,5]
    print(s.VerifySquenceOfBST(sequence))
