def sum_col_2d(list):
    # Alternative solution: [max(col) for col in zip(*sample_list)]
    sum_col = []
    for index in range(len(list[0])):
        #print(index)
        column_sum = 0
        for row in list:
            #print(row)
            column_sum += row[index]
            #print(column_sum)
        sum_col.append(column_sum)
    return sum_col

print (sum_col_2d([[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]))
