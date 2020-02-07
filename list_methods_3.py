# Function that accepts two positives integers a and b (a < b)
# and returns a list that contains all the odd numbers between a and b
# (including a and b if applicable) in descending order.

def odd_numbers(a, b):
    lst = []
    number = b
    while number > a:
        if number % 2 != 0:
            lst.append(number)
        number = number - 1
    return lst

print (odd_numbers(11, 31))
