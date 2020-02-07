###### MY CODE ######
def unique_common(a, b):
    test_list = []

    for i in a:
        if i in b:
            test_list.append(i)
    if not test_list:
        return None

    common_list = []
    for i in test_list:
        if i not in common_list:
            common_list.append(i)
    return sorted(common_list)

print (unique_common([5, 6, 7, 0], [3, 2, 3, 2]))


###### INSTRUCTOR CODE ######
def unique_common_elements_sample_ed(a, b):
    common = []
    for items in a:
        if items in b:
            common.append(items)
    if not common:
        return None
    
    unique = []
    for items in common[:]:
        if items not in unique:
            unique.append(items)
    return sorted(unique)





