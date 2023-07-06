#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list2 = [[1, -3, 2], [-3, -1, 3], [5, -3, 0]]
print(matrix_mul(list1, list2))
print(matrix_mul(None, None))
print(matrix_mul([[1, 2, 3]], [[3], [5], [8]]))
print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))
