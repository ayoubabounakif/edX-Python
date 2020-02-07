#program which asks the user to type a positive integer n
#and then prints the sum of the square of all numbers
#from 1 to n (including both 1 and n).

#For example if the user type 3
#the answer should be ((3**2) + (2**2) + (1**2)) = 14

#                           CODE

ask_user = input("Input a positive integer n:")
n = int(ask_user)

i = 1
sum = 0

for i in range(1, n+1):
    sum = sum + (i**2)
    
print (sum)



