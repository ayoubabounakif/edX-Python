###### MY CODE ######
from assignment_2 import find_mismatch
from assignment_2_2 import single_insert_or_delete

def spelling_corrector(string, correct_spell):
    string = string.strip().split()
    output_str = ""
    for word in string:
        if len(word) <= 2 or word in correct_spell:
            output_str = output_str + " " + word
            continue
        min_mismatch = 2
        replacement_word = word
        for correct_word in correct_spell:
            if min(find_mismatch(word, correct_word), single_insert_or_delete(word, correct_word)) == 1:
                replacement_word = correct_word
                break
        output_str = output_str + " " + replacement_word
    return output_str.strip().lower()

###### INSTRUCTOR CODE ######
def instructor_function(string, correct_spelled):
    words = string.strip().split()
    output_str = ""
    for current_word in words:
        if len(current_word) <= 2 or (current_word in correct_spelled):
            output_str = output_str + " " + current_word
            continue
        min_mismatch = 2
        replacement_word = current_word
        for correct_word in correct_spelled:
            if min(find_mismatch(current_word,correct_word), single_insert_or_delete(current_word,correct_word)) == 1:
                replacement_word = correct_word
                break
        output_str = output_str + " " + replacement_word
    return output_str.strip().lower()

def find_mismatch(s1,s2):
    if len(s1) != len(s2):
        return 2
    s1=s1.lower()
    s2=s2.lower()
    number_of_mismatches=0
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            number_of_mismatches=number_of_mismatches+1
            if number_of_mismatches>1:
                return 2
    return number_of_mismatches


def single_insert_or_delete(s1,s2):
    s1=s1.lower()
    s2=s2.lower()
    if s1==s2:
        return 0
    if abs(len(s1)-len(s2))!=1:
        return 2

    if len(s1)>len(s2):
        # only deletion is possible
        for k in range(len(s2)):
            if s1[k]!=s2[k]:
                if s1[k+1:]==s2[k:]:
                    return 1
                else:
                    return 2
        return 1
    else: # s1 is shorter Only insertion is possible
        for k in range(len(s1)):
            if s1[k]!=s2[k]:
                if s1[k:]==s2[k+1:]:
                    return 1
                else:
                    return 2
        return 1
