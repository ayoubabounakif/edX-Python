####### MY CODE #######

def items_price(a, b):
    quantity = a
    prices = b
    c = [a*b for a,b in zip(a,b)]
    total = sum(c)
    return total

print (items_price([2, 3, 5, 7, 9], [5, 8, 4, 1, 11]))

####### EDX CODE #######
def items_price_edx(a, b):
    result = 0
    for i in range(0, len(a)):
        result += a[i] * b[i]
    return result

