###### MY CODE ######
def find_mismatch(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    count = 0
    if str_1 == str_2:
        return 0
    elif len(str_1) == len(str_2):
        count = 0
        for i in str_1:
            if i not in str_2:
                count += 1
        if count == 1:
            return 1
        else:
            return 2
    elif len(str_1) != len(str_2):
        if str_1 != str_2:
            for i in str_1:
                if i not in str_2:
                    count += 1
        return 2

###### INSTRUCTOR CODE ######
def instructor_function(s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    mismatches = 0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            mismatches = mismatches + 1
            if mismatches > 1:
                return 2
    return mismatches
