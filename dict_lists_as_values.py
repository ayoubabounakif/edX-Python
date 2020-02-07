def lists_values(dict):
    output_list = []
    keys = dict.keys()
    #print(keys)
    for k in keys:
        list = dict[k]
        #print(list)
        grade1, grade2, grade3, = list[0], list[1], list[2]
        #print (grade1, grade2, grade3)
        if grade1 >= 78 and grade2 >= 78 and grade3 >= 78:
            output_list.append(k)
            #print (k)
    return output_list

print (lists_values({'Hectar': [80, 50, 0], 'John': [70, 80, 85], 'Undertaker': [90, 92, 93]\
    ,'Priest': [75, 78, 83], 'Henry': [80, 85.2, 88]}))
