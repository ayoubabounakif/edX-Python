###### MY CODE ######
from fractions import gcd
from functools import reduce

def find_gcd(list):
    x = reduce(gcd, list)
    return x

print (find_gcd([3, 5, 9, 11, 13]))



###### INSTRUCTOR CODE ######
def sample_gcd_list_edx(my_list):
    result = my_list[0]
    for i in range(1, len(my_list)):
        result = gcd_edx(result, my_list[i])
    return result
  
def gcd_edx(a,b):
    while b:
        a, b = b, a%b
    return a


