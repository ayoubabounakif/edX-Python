# Function that accepts two positive integers as function parameters and
# returns their least common multiple (LCM). The LCM of two integers a and b is
# the smallest (non zero) positive integer that is divisible by both a and b.
# For example, the LCF of 4 and 6 is 12, the LCM of 10 and 5 is 10.

# CODE


def lcm(x, y):
   if x > y: # Choose the greatest number
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm


    

