#!/usr/bin/python3
'''Has a function that returns a list of lists of integers representing
   the Pascal’s triangle of n
'''


def pascal_triangle(n):
    '''
    Creates a pascal's triangle.

    Args:
        n (int): The number to represents its pascal's triangle.

    Returns:
        list of lists (int): representing the pascal's triangle
    '''
    triangle = []
    if n <= 0:
        return triangle
    triangle.append([1])

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row += [1]
        triangle.append(row)

    return triangle
