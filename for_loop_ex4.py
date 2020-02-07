#program that asks the user for an input 'n'
#(assume that the user enters a positive integer)
#and prints a sequence of powers of 10 from 10^0 to 10^n in separate lines.
#For example if 'n' is equal to 4, the output should be like the one below!
"""
1
10
100
1000
10000

"""

n = int(input("Type a positive integer n:"))
i = 0

for i in range (0,n+1):
    x = 10**i 
    print(x)


