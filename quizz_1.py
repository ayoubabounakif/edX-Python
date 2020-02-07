#a program that asks the user for an integer 'x' 
#and prints the value of y after evaluating the following expression:
#y = x^2 - 12x + 11

import math
ask_user = input("Please enter an integer x:")

x = int(ask_user)
y = math.pow(x,2) - 12*x + 11

print(int(y))
