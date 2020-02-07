def convert_2d_1d(list):
    output_list = []
    for x in list:
        for index in x:
            output_list.append(index)
            output_list.sort()
            #print (output_list)
    return output_list

print (convert_2d_1d([[0, 2, 4, 6, 8, 10], [11, 18, 19, 110, 111, 112]]))
