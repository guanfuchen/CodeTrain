#!/usr/bin/python
# -*- coding: UTF-8 -*-

# bubblesort就是不断将大的数往后移
def bubblesort(array):
    array_len = len(array)
    for i in range(array_len):
        for j in range(array_len-i-1):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp

if __name__ == '__main__':
    array = [1, 5, 4, 3, 2]
    bubblesort(array)
    print('array:', array)
    pass
