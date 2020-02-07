# Write a function that accepts a positive integer k and returns the list
# of all the divisors of k.
# Your list should include both 1 and k.


import math
def divisors(k):
    lst = []
    for i in range (1, k+1):
        # Check for the remainder when k is divided by i
        if k % i == 0: # if the remainer is 0 that means i is a divisor of k
            lst.append(i) # append i to the list stored in the variable called lst
            lst.sort() # sort it 
    return lst

print (divisors(10))






