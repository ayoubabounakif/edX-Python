def count_rows_even_odd_2d(list):
    count_even = 0
    count_odd = 0
    for row in list:
        row_sum = sum(row)
        if row_sum % 2 == 0:
            count_even = count_even + 1
        else:
            count_odd = count_odd + 1
    return [count_even, count_odd]

print (count_rows_even_odd_2d([[0, 0, 2, 3], [5, 5, 5, 5], [37, 37, 37, -39]]))
