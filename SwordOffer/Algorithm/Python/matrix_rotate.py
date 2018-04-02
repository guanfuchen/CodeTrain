#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix:
                matrix = self.turn(matrix)

        return result

    def turn(self, matrix):
        print(matrix)
        row = len(matrix)
        col = len(matrix[0])

        new_matrix = []
        for row_index in range(row):
            new_matrix_row = []
            for col_index in range(col):
                new_matrix_row.append(0)
            new_matrix.append(new_matrix_row)

        turn_list = []
        for row_index in range(row):
            turn_list.append(matrix[row_index][col-1])
        for col_index in range(col-2, -1, -1):
            turn_list.append(matrix[row-1][col_index])
        # print(turn_list)


        for col_index in range(col):
            new_matrix[0][col_index] = turn_list.pop(0)

        for row_index in range(1, row, 1):
            new_matrix[row_index][col-1] = turn_list.pop(0)

        # print(new_matrix)
        for row_index in range(1, row):
            for col_index in range(0, col - 1):
                new_matrix[row_index][col_index] = matrix[row_index - 1][col_index]

        # print(new_matrix)
        return new_matrix

if __name__ == '__main__':
    s = Solution()
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print(s.printMatrix(matrix))
