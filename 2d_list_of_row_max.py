def row_max_2d(list):
    max_row = []
    for row in list:
        max_row.append(max(row))
    return max_row

print (row_max_2d([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))
