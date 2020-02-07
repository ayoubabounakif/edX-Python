def integer_most_divisors(list):
    max_divisors = 0
    max_divisors_item = None

    for items in list:
        output_list = []
        for number in range(1, items):
            if items % number == 0:
                output_list.append(number)

        length = len(output_list)
        if length > max_divisors:
            max_divisors = length
            max_divisors_item = items

    return max_divisors_item

print (integer_most_divisors([8, 12, 18, 6]))


######### MY CODE #########

def my_fun(list):
    output_list = []
    for i in list:
        c = 0
        for n in range(1, i+1):
            if i % n == 0:
                c += 1
        output_list.append(c)

    return list[output_list.index(max(output_list))]

#print (my_fun([8, 12, 18, 6]))
