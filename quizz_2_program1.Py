#Write a program which asks the user to enter their age in years
#(Assume that the user always enters an integer)
#and based on the following conditions, prints the output
#exactly as in the following format
#When age is less than or equal to 0, your program should print -> UNBORN
#When age is greater than 0 and less than or equal to 150, your program should
#print -> ALIVE
#When age is greater than 150, your program should print -> VAMPIRE

#               Code

ask_user = input("Please enter your age:")
ask_user = int(ask_user)

if ask_user <= 0:
    print ("UNBORN")

if 0 < ask_user <= 150:
    print ("ALIVE")

if ask_user > 150:
    print ("VAMPIRE")
