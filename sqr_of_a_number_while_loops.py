#Calculating the sq root of a number
import random

ask_user = input("Enter a number:")
number = float(ask_user)
guess = number / 2
accuracy = 0.01
iteration = 0

while abs(number - (guess ** 2)) > accuracy:
    print ("Iteration", iteration, "Guessed sqr is :", guess)
    guess = (guess + (number / guess)) / 2
    iteration = iteration + 1
    
print ("Original number is:", number)
print ("Square root of the number is:", guess)
 
