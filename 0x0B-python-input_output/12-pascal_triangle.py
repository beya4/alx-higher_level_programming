#!/usr/bin/python3
"""
Returns a list of lists of integers repres the Pascal
"""


def pascal_triangle(n):
    """
    Pascal’s triangle of n
    """
    pascal_trian = [[1]] if n > 0 else []
    for x in range(1, n):
        row = []
        for y in range(x + 1):
            if (y == 0 or y == x):
                row.append(1)
            else:
                row.append(pascal_trian[x - 1][y - 1] + pascal_trian[x - 1][y])
        pascal_trian.append(row)
    return pascal_trian
