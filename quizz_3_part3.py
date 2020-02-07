# Function that returns the sum of all the odd numbers in a list given.
# If there are no odd numbers in the list, your function should return 0 as the sum.

# CODE
def sumOfOddNumbers(numbers_list):
    total = 0
    count = 0
    for number in numbers_list:
        if (number % 2 == 1):
            total += number
    if (number == count):
        return (0)
    return total


