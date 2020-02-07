def perform_multiplication(integer_1, integer_2):
    integer_2 = integer_1 * integer_2
    return integer_1, integer_2
integer_1, integer_2 = perform_multiplication(8, 11)
print(integer_1, integer_2)


def test():
    x=7
x = 11
test()
print(x)


def test():
    global x
    x=7
x = 11
test()
print(x)


def test(x):
    x=8
x = 5
test(x)
print(x)


def test(x):
    x = 7
x = 11
x = test(x)
print(x)


def evaluate_expression_1(x):
    x = x + 5
    def evaluate_expression_2(x):
        return x
    return x
scholar = 1008
print(evaluate_expression_1(scholar))


def evaluate_expression_1():
    global x
    x = x + 5
    def evaluate_expression_2():
        return None
    return x
x = 33
print(evaluate_expression_1())


def evaluate_expression_1():
    global x
    x = x - 3
    def evaluate_expression_2():
        global x
        return x + 7

    return evaluate_expression_2()
x = 33
print(evaluate_expression_1())


def evaluate_expression_1(x):
    x = x - 3
    def evaluate_expression_2():
        global x
        return x + 7
    return evaluate_expression_2()
x = 7
print(evaluate_expression_1(x))
