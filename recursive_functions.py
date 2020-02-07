def factorial(number):
    result = 1
    for k in range(number, 1, -1):
        result = result * k
    return result


print(factorial(10))


def recursive_factorial(number):
    # base case
    if number < 1:
        return 1
    else:  # recursive call
        return number * recursive_factorial(number-1)


output = recursive_factorial(7)
print("The factorial of", 7, "is =", output)


def recursive_sum(n):
    if n == 1:  # base case
        return 1
    return (recursive_sum(n-1)+n)


print("Sum of 1 through", 10, "is =", recursive_sum(10))


def calculate_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)


print(calculate_fibonacci(10))  # Output == 55


def calculate_factorial(n):
    if n < 2:  # base case
        return 1
    else:  # recursive call
        return n * calculate_factorial(n-1)


print(calculate_factorial(5))


def calculate_exponent(a, b):
    if b == 0:  # base case
        return 1
    else:   # recursive call
        return a * calculate_exponent(a, b-1)


print(calculate_exponent(5, 3))


def calculate_gcd(a, b):
    r = a % b
    if r == 0:
        return b
    elif r == 1:
        return 1
    return calculate_gcd(b, r)


print(calculate_gcd(10, 15))


def gcd_recursion_sample(a, b):
    if b == 0:  # base case
        return a
    else:   # recursive call
        return gcd_recursion_sample(b, a % b)


def nested_list_sum(n):
    ___ = 0
    for element in n:
        if isinstance(element, int):  # if type (element) != type([])
            ___ += element
        else:
            ___ += nested_list_sum(element)
    return ___


print(nested_list_sum([1, -1, [2, -2], [3, -3, [4, -4], 10]]))  # 10
