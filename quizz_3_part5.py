# Function that accepts a positive integer n as function parameter and returns 'True'
# if n is a prime number, 'False' otherwise. Note that zero and one are not prime numbers
# and two is the only prime number that is even.

def prime_num(n):
    n = abs(int(n)) # Check that n is a positive integer.
    if n < 2: # 0 and 1 are not primes
        return False

    if n == 2: # 2 is the only even prime number
        return True    

    if not n & 1: # all other even numbers are not primes
        return False
    
    for x in range(3, int(n**0.5) + 1, 2): # range starts with 3 and only needs to go up \ 
        if n % x == 0:                     # the square root of n for all odd numbers
            return False
    return True


