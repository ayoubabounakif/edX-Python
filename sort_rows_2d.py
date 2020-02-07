###### MY CODE ######
def sort_rows_2d(list):
    output_list = []
    for row in list:
        row.sort(reverse=True)
        output_list.append(row)
    return output_list

print (sort_rows_2d([[0, 2, 4, 6, 8, 10], [11, 18, 19, 110, 111, 112]]))

###### INSTRUCTOR CODE ######
def _2d_rows_sorted(_2d_list):
    for rows in _2d_list:
        rows.sort(reverse=True)
    return _2d_list
