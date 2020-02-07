def return_keys(dict, value):
    sorted_list = []
    keys = dict.keys()
    for k in keys:
        if value in dict[k]:
            sorted_list.append(k)
    sorted_list.sort()
    return sorted_list


dict = {"rabbit" : [1, 2, 3],
          "kitten" : [2, 2, 6],
          "lioness": [6, 8, 9]}
print (return_keys(dict, 2))
