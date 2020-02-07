def sum_rows_2d(list):
    sum_row = []
    for row in list:
        sum_row.append(sum(row))
    return sum_row

print (sum_rows_2d([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))
