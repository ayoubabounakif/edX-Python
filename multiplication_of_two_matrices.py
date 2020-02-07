###### MY CODE ######
def multiply_matrices(mat_1, mat_2):
    output = []
    iteration_col = 0
    iteration_row = 0
    for col in range(len(mat_1[0])):
        iteration_col = iteration_col + 1
    for row in mat_2:
        iteration_row = iteration_row + 1
    if iteration_col == iteration_row:
        output = [[sum(a * b for a, b in zip(mat_1_row, mat_2_col)) for mat_2_col in zip(*mat_2)] for mat_1_row in
                  mat_1]
    return output


###### INSTRUCTOR CODE ######
def multiply_matrices_edx(a, b):
    if len(a[0]) != len(b):
        return None
    # Create the result matrix and fill it with zeros
    output_list = []
    temp_row = len(b[0]) * [0]
    for r in range(len(a)):
        output_list.append(temp_row[:])
    for row_index in range(len(a)):
        for col_index in range(len(b[0])):
            sum = 0
            for k in range(len(a[0])):
                sum = sum + a[row_index][k] * b[k][col_index]
            output_list[row_index][col_index] = sum
    return output_list


###### USING numpy ######
def product_matrices(matrice_a, matrice_b):
    import numpy
    product = (numpy.mat(matrice_a) * numpy.mat(matrice_b))  # Returns a numpy array
    output = product.tolist()  # Convert the numpy array to a list
    return output


print (product_matrices([[12, 7, 3],  # mat_1 (START)
                         [4, 5, 6],
                         [7, 8, 9]],  # mat_1 (END)
                        [[5, 8, 1, 2],  # mat_2 (START)
                         [6, 7, 3, 0],
                         [4, 5, 9, 1]]))  # mat_2 (END)

print (product_matrices([[12, 7, 3],  # matrice_a (START)
                         [4, 5, 6],
                         [7, 8, 9]],  # matrice_a (END)
                        [[5, 8, 1, 2],  # matrice_b (START)
                         [6, 7, 3, 0],
                         [4, 5, 9, 1]]))  # matrice_b (END)

print (multiply_matrices_edx([[2, 3, 54],  # a (START)
                              [3, 4, 5]],  # a (END)
                             [[4, -3, 212],  # b (START)
                              [1, 1, 15],
                              [1, 3, 122]]))  # b (END)
