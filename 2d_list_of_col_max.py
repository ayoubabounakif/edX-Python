def max_col_2d(list):
    output_list = []
    for col in range(len(list[0])):
        column_max = 0
        for row in list:
            if row[col] > column_max:
                column_max = row[col]
        output_list.append(column_max)
    return output_list

print (max_col_2d([[1, 1, 1, 12], [10, 2, 2, 2], [3, 3, 20, 3], [4, 40, 4, 4]]))
