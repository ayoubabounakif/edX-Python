def multiplication_check_matrices(mat_1, mat_2):
    iteration_col = 0
    iteration_row = 0
    for col in range(len(mat_1[0])):
        iteration_col = iteration_col + 1
    for row in mat_2:
        iteration_row = iteration_row + 1
    if iteration_col == iteration_row:
        return True
    else:
        return False

a = [[2, 3, 4],
     [3, 4, 5]]
b = [[4, -3, 12],
     [1, 1, 5],
     [1, 3, 2]]

print (multiplication_check_matrices(a, b))
