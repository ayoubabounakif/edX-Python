#Write a program which asks the user to type a string and then: 
#Print "Dog" if the word "dog" exists in the input string.
#Print "Cat" if the word "cat" exists in the input string.
#(if both "dog" and "cat" exist in the input string, then you should only print "Dog") 
#Otherwise prints "None". (Pay attention to capitalization).

#                   Starting Code

ask_user = input("Please type a string:")

x = "dog" and "cat"

if "dog" in ask_user:
    print ("Dog")
    
elif "cat" in ask_user:
    print("Cat")

elif x in ask_user:
    print("Dog")

else:
    print("None")

