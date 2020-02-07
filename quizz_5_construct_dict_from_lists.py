###### MY CODE ######
def construct_dictionary_from_lists(names_list, ages_list, scores_list):
    new_dict = {i:[j, k] for i, j, k in zip(names_list, ages_list, scores_list)}
    for key, value in new_dict.items():
        if value[1] >= 60:
            value.append('pass')
        else:
            value.append('fail')
    return new_dict

###### INSTRUCTOR CODE ######
def create_dictionary_from_list_q5_sample(names, ages, scores):
    sample_dict = {}
    for index in range(0, len(names)):
        if scores[index] >= 60:
            sample_dict[names[index]] = [ages[index], scores[index], "pass"]
        else:
            sample_dict[names[index]] = [ages[index], scores[index], "fail"]
    return sample_dict
#return {names_list[i] : ages_list[i] for i in range(len(names_list))}
#my_dict_3 = dict(zip(names_list, zip(ages_list, scores_list)))

print (construct_dictionary_from_lists(['paul', 'saul', 'steve', 'chimpy'], [28, 59, 22, 5], [59, 85, 55, 60]))
