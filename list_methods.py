# Function that accepts a positive integer k and returns a list that contains
# the first five multiples of k.
# The multiples should be calculated starting from 1 to 5 (Included).

def multiples(k):
    lst = []
    for i in range(1, 5+1):
        mtp = k * i
        lst.append(mtp)
    return lst
            



