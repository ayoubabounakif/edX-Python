def max_even_2d(list):
    even = []
    for x in list:
        for index in x:
            if index % 2 == 0:
                even.append(index)
    if even == []:
        return None

    maximum = even[0]
    for num in even:
        if num > maximum:
            maximum = num
    return maximum

print (max_even_2d([[121, -18, 20, 13, -44], [199, -12, -6, 13, -44]]))
