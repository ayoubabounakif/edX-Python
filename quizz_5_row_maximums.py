def maximum_rows(list_2d):
    def calculate_max(list):
        my_max = list[0]
        for number in list:
            if number >= my_max:
                my_max = number
        return my_max

    output_dictionary = {}
    list_of_max = []
    for row in list_2d:
        my_max = calculate_max(row)
        list_of_max.append(my_max)
        #list_of_max.sort()
        #print (list_of_max)
    for x in range(len(list_of_max)):
        #print (x)
        my_str = 'row ' + str(x) + ' max'
        output_dictionary[my_str] = list_of_max[x]
    return output_dictionary


################### Instructor function ###################
"""def _max_of_each_row_sample_q5(my_multidimensional_list):
    def calculate_my_max(some_list):
        sample_max = some_list[0]
        for number in some_list:
            if number >= sample_max:
                sample_max = number

        return sample_max

    list_of_max = []
    for rows in my_multidimensional_list:
        my_max = calculate_my_max(rows)
        list_of_max.append(my_max)
    #my_sorted_list = sorted(list_of_max)
    my_dict = {}
    for x in range(0, len(list_of_max)):
        my_string = 'row' + " " +  str(x) + " " + 'max'
        my_dict[my_string] = list_of_max[x]

    return my_dict"""
