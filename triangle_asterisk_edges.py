ask_user = int(input("Enter a positive integer: "))
if ask_user > 1:
    print ('*' * ask_user) # Print the top line
    for i in range(ask_user-1, 1, -1):
        print ('*'+(i-2) * " " +"*") # Print the middle lines
    print ('*') # Print the bottom line
elif ask_user == 1:
    print ('*')

# First of all the expression "for x in range (n -1,1,-1)"
# means the starting number of x is the first number in the parenthesis
# which is (n-1) and the ending number for x is the number right before 1
# which is of course the number 2, the -1 indicate that x is DECREASING by 1.
# For example, the expression "for k in range (6,1,-1)
# means the values for k are 6,5,4,3 and 2.
# Thus for a specified value of n the expression "for x in range (n-1,1,-1)"
# actually produce a sequence of decreasing x that starts at (n-1) and ends at 2.
# In the print statement, the expression (x-2)* " "
# means the empty space represented by " " is to be multiplied the number (x-2).
# And remember the number x is deceasing,
# thus the amount of empty space is starting with a big number and decreasing by 1
# in each step in accordance to the decrease in x.
# Thus the print statement "print ("" + (x-2)" " + "*")
# actually means, "asterisk plus long line of empty space plus asterisk".
# The line of empty space is going to decrease by 1 in each step.

# For example if n = 10, then x = 9,8,7,6,5,4,3,2, then (x - 2) = 7,6,5,4,3,2;
# then computer will print; * (7 empty space) *, then * (6 empty space) *, and so on...
