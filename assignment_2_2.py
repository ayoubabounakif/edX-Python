###### MY CODE ######
def single_insert_or_delete(str_1, str_2):
    str_1, str_2 = str_1.lower(), str_2.lower()
    if str_1 == str_2:
        return 0

    elif len(str_1) == len(str_2):
        return 2

    elif len(str_1) - len(str_2) == -1:
        if str_1 == str_2[:-1]:
            return 1
        else:
            for i in range(len(str_2)):
                if str_1 == str_2[:i]+ str_2[i+1:]:
                    return 1
            else:
                return 2

    elif len(str_1) - len(str_2) == 1:
        if str_1[:-1] == str_2 or str_1[1:] == str_2:
            return 1
        else:
            for i in range(len(str_1)):
                if str_1[:i]+ str_1[i+1:] == str_2:
                    return 1
            else:
                return 2
    else:
        return 2

###### INSTRUCTOR CODE ######
def instructor_function(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # Only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter; Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
