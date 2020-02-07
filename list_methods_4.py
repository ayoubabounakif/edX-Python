# Function that acceptes a positive integer k and returns the ascending sorted
# list of cube root values of all the numbers from 1 to k
# (including 1 and not including k)
# if k is 1, your program should return and empty list

def lst_cube_root(k):
    lst = []
    for i in range(1, k):
        cube_root = i ** (1/3)
        lst.append(cube_root)
        if k == 1:
            return []
    return lst

print (lst_cube_root(100))



