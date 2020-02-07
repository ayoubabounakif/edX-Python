#Write a program which asks the user to type an integer.
#If the number is 2  then the program should print "two",
#If the number is 3  then the program should print "three",
#If the number is 5  then the program should print "five", 
#Otherwise it should print "other".

#                   Start Code

ask_user = input("Please type an integer: ")
number = int(ask_user)

if number == 2:
    print("two")
elif number == 3:
    print("three")
elif number == 5:
    print("five")
else:
    print("other")

