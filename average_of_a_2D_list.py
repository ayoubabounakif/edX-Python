def avg_2d(list):
    sum = 0
    count = 0
    for row in range(len(list)):
        for column in range(len(list[row])):
            count = count + 1
            sum = sum + list[row][column]
            avg =  sum / count
    return avg

print (avg_2d([[0, 0, 2, 3], [5, 5, 5, 5], [37, 37, 37, -39]]))
