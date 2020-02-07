# Function that accepts a list of integers and returns the average.
# Assuming that the input list contains only numbers.
# Do NOT use the build-in sum() function.

# CODE (Calculate average of a list)
def avg(testlist):
    summ = 0
    for i in testlist:
        summ = summ + i

    length_list = len(testlist)
    average = summ / length_list
    return average
