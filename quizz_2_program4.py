#Write a program that asks the user to enter a positive integer n.
#Assuming that this integer is in seconds,
#your program should convert the number of seconds into days, hours, minutes, and seconds
#and prints them exactly in the format specified below.

#Here are a few sample runs of what your program is supposed to do:

#when user enters : ---> 369121517
#your program should print:
#       4272 days 5 hours 45 minutes 17 seconds

#when user enters : ---> 24680
#your program should print:
#       0 days 6 hours 51 minutes 20 seconds

#when user enters : ---> 129600
#your program shoudl print:
#       1 days 12 hours 0 minutes 0 seconds

#                   CODE

#1 minute = 60 seconds
#1 hours = 60 * 60 = 3600 seconds
#1 day = 60 * 60 * 24  = 86400 seconds

sec = int(input("Enter the number of seconds:"))

time = int(sec)

days = time // 86400
hours = (time - (days * 86400)) // 3600
minuts = (time - ((days * 86400) + (hours * 3600)) ) // 60
seconds = (time - ((days * 86400) + (hours * 3600) + (minuts * 60)))

print (days, 'days' ,hours,'hours',minuts, 'minutes',seconds,'seconds')
    
