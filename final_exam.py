###### CODE ######
def n_letter_dictionary_final_sp(my_string):
    my_dict = {}
    my_list = my_string.strip().split()
    for word in my_list:
        length=len(word)
        lowered_word=word.lower()
        if my_dict.get(length):
            if lowered_word not in my_dict[length]:
                my_dict[length].append(lowered_word)
                my_dict[length].sort()
        else:
            my_dict[length]=[lowered_word]
    return my_dict


###### CODE ######
    def my_final_grades_sample_f(file_name):
        fp = open(file_name, "r")
        data = fp.readlines()
        my_dictionary = {}
        for x in range(0, len(data)):
            stripped = data[x].strip().split(',')
            for x in range(1, len(stripped)):
                stripped[x] = int(stripped[x].strip())

            # extract various parts from each line
            name = stripped[0].lower()
            quizzes = stripped[1:7]
            assignments = stripped[7:11]
            midterm = int(stripped[11])
            final = int(stripped[12])

            # deal with the quizzes # remove the two minimum quizzes
            quizzes.remove(min(quizzes))
            quizzes.remove(min(quizzes))

            # deal with the assignments # remove one of the minimum assignment
            assignments.remove(min(assignments))

            # calculate the percentage of each score based on 25%
            quiz_score = (sum(quizzes)/len(quizzes)) * 0.25
            assignment_score = (sum(assignments)/len(assignments)) * 0.25
            midterm_score = midterm * 0.25
            final_score = final * 0.25

            # calculate total score
            total_score = quiz_score + midterm_score + assignment_score + final_score
            # print("q =", quizzes, quiz_score)
            # print("assign =", assignments, assignment_score)
            # print("midterm, final", midterm_score, final_score)
            # print("total_score", total_score)
            if total_score >= 60:
                my_dictionary[name] = "pass"
            else:
                my_dictionary[name] = "fail"
        return my_dictionary


###### CODE ######
def my_pattern(n):
    tree = [[1]]
    for x in range(1, n):
        m = [1]
        for y in range(1, x):
            m.append(tree[x-1][y-1] + tree[x-1][y])
        m.append(1)
        tree.append(m)
    return tree

###### CODE ######
def _dictionary_of_word_counts_sample_(sample_string):
    lowered_splitted_string = sample_string.lower().split()
    sample_dictionary = {}
    for word in lowered_splitted_string:
        sample_dictionary[word] = lowered_splitted_string.count(word)
    return sample_dictionary
