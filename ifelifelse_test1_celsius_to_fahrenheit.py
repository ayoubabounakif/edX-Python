#Write a program to:
#Get an input temperature in Celsius
#Convert it to Fahrenheit
#Print the temperature in Fahrenheit
#If it is below 32 degrees print "It is freezing"
#If it is between 32 and 50 degrees print "It is chilly"
#If it is between 50 and 90 degrees print " It is OK"
#If it is above 90 degrees print "It is hot"

#                   Code Starts Here

user_input = input("Please input a temperature in Celsius:")

celsius = float(user_input)
fahrenheit = ((celsius * 9) / 5 ) +32

print ("The temperature is ",fahrenheit, "degrees Fahrenheit")

if fahrenheit < 32:
    print ("It is freezing")
    
elif 32 <= fahrenheit <= 50:
    print ("It is chilly")
    
elif 50 < fahrenheit < 90:
    print ("It is OK")
    
elif fahrenheit >= 90:
    print ("It is hot")



