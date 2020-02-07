###### MY CODE ######
def sum_2d(list):
    sum = 0
    for row in range(len(list)):
        for column in range(len(list[0])):
            sum = sum + list[row][column]
    return sum

print (sum_2d([[-18, 20, 13, 44], [-12, -6, 13, -44]]))
    
