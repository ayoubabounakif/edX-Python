                    #ALGORITHM
'''
    1. Select a number
    2. Select a divisor and set it equal to 2.
    3. Assume number is prime
    4. If divisor is less then the number go to step 5 else go to step 8
    5. If remainder of (number/divisor) is 0 then number is not prime(exit/stop)
    6. Add one to the divisor
    7. Go to step 4
    8. Number is prime
    
'''
# A program that prints the prime numbers
#between x (start_number) and y (end_number)

            #CODE (using while loop)

ask_user = int(input("Enter a value for x: "))
ask_user_2 = int(input("Enter a value for y: "))

x = ask_user 
y = ask_user_2
current_number = x

while current_number <= y:
    current_divisor = 2
    current_number_prime = True
    
    while (current_divisor < current_number):
        if current_number % current_divisor == 0:
            current_number_prime = False
            break
        current_divisor = current_divisor + 1
        
    if current_number_prime:
        print (current_number, "is prime")
    current_number = current_number + 1
    
print ("DONE! These are all the prime numbers between your values!")

            #CODE (using for loop)

ask_user = int(input("Enter a value for x: "))
ask_user_2 = int(input("Enter a value for y: "))

x = ask_user 
y = ask_user_2
current_number = x

for current_number in range(x, y+1):
    current_number_prime = True
    
    for current_divisor in range (2, current_number):
        if current_number % current_divisor == 0:
            current_number_prime = False
            break
        
    if current_number_prime:
        print (current_number, "is prime")
    
print ("DONE! These are all the prime numbers between your values!")
