# Function that accepts two positive integers a and b and returns
# a list of all the even numbers between a and b (including a and not b)

def even_numbers(a, b):
    lst = []
    for number in range(a, b):
        if number % 2 == 0:
            lst.append(number)
    return lst

print (even_numbers(50,100))
