#program which asks the user to type an integer n
#and then prints the sum of all numbers from 1 to n (including both 1 and n).

#                   CODE

ask_user = input("Type an integer n:")
n = int(ask_user)
i = 1
sum = 0

for i in range(1, n+1):
    sum = sum + i

print (sum)
