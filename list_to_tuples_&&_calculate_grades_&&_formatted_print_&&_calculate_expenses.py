# Commented codes will output and Error

"""my_string = "x = {1:5.2f} and y = {0:3d}".format(14, 3.5)
print(my_string)

my_string = "x = {} and y = {}".format(5, "pet")
print(my_string)


# my_string = "x = {} and y = {}".format(2.3)
# print(my_string)


my_string = "x = {2} and y = {1}".format("cat", 2.3, "pet")
print(my_string)

my_string = "x = {1:5.2f} and y = {0:5d}".format(13, 5.2645326)
print(my_string)

# my_string = "x = {0:4d} and y = {1:3d}".format("dog", 1)
# print(my_string)

my_string = "x = {0:#^7d} and y = {1:@>8.3f}".format(2, 0.6)
print(my_string)

a = "jack"
b = "sad"
my_string = "{0:*^12} is {1:+^7s}".format(a, b)
print(my_string)

print('X{0:Y^9}Z'.format('cat'))

print('B{0:,}C'.format(123456789))"""


def nested_list_to_nested_tuple(list_2d):
    reversed_list = [t[::-1] for t in list_2d]
    outter_tuple = tuple(reversed_list)
    return tuple([tuple(l) for l in outter_tuple])


def _nested_list_to_nested_tuple(_list_2d):
    for items in _list_2d:
        items = items.reverse()
    for x in range(0, len(_list_2d)):
        _list_2d[x] = tuple(_list_2d[x])
    return tuple(_list_2d)


# print(_nested_list_to_nested_tuple([['mean', 'really', 'is', 'jean'],
    #         ['world', 'my', 'rocks', 'python']]))


def calculate_grades(file_name):
    file_pointer = open(file_name, 'r')
    # You can use either .read() or .readline() or .readlines()
    data = file_pointer.readlines()
    students_list = []
    for each_line in data:
        name, quiz1, quiz2, quiz3, quiz4 = each_line.strip().split(',')
        quiz_average = (float(quiz1) + float(quiz2) + float(quiz3) + float(quiz4)) / 4
        students_list.append((name, quiz_average))
    # Reverse
    myTuple = tuple(students_list)
    return sorted(myTuple)


# Complex way of the reverse
''' # unSorted = True
    # while unSorted:
        # unSorted = False
        # for index in range(0, len(students_list)-1):
        # if next element is greater element then swap them
            # if students_list[index][0] > students_list[index + 1][0]:
                # temporary_variable = students_list[index]
                # students_list[index] = students_list[index + 1]
                # students_list[index + 1] = temporary_variable
                # unSorted = True '''

# print(calculate_grades('students_grades_2'))


# ###Instructor's Solution ###
def dict_to_print(a):
    my_names = list(a.keys())
    my_scores = list(a.values())

    # Sort the information by score descending order
    unSorted = True
    while unSorted:
        unSorted = False
        for index in range(0, len(my_scores)-1):
            # if next element is greater element then swap them
            if my_scores[index] < my_scores[index + 1]:
                # sort the scores
                temporary_score = my_scores[index]
                my_scores[index] = my_scores[index + 1]
                my_scores[index + 1] = temporary_score
                # sort the names as well
                temporary_name = my_names[index]
                my_names[index] = my_names[index + 1]
                my_names[index + 1] = temporary_name

                unSorted = True
    for x in range(0, len(my_names)):
        print("{0:<10s}{1:>6.2f}".format(my_names[x], my_scores[x]))


# #### MY CODE ####
def formatted_print(my_dictionary):
    x = sorted(my_dictionary.items(), key=lambda kv: kv[1], reverse=True)
    for i in x:
        my_names = list(i)[0]
        my_scores = list(i)[1]
        print("{0:<10s}{1:>6.2f}".format(my_names, my_scores))


# print(formatted_print({'john': 34.480, 'eva': 88.5, 'alex': 90.55, 'tim': 65.900}))

my_file = open("expenses.txt", "w")
my_file.write("milk,2.35\n \
bread , 1.95\n \
 chips ,    2.54\n \
milk  ,    2.38\n \
milk,2.31\n \
bread,    1.90")
my_file.close()


def calculate_expenses(filename):
    my_dictionary = {}
    # Make a connection to the file
    file_pointer = open(filename, 'r')
    data = file_pointer.readlines()
    for line in data:
        line = line.strip().split(',')
        my_item = line[0].strip()
        my_price = float(line[1].strip())
        if my_item not in my_dictionary:
            my_dictionary[my_item] = my_price
        else:
            my_dictionary[my_item] += my_price
    my_list = []
    my_keys = sorted(my_dictionary.keys())
    for x in my_keys:
        my_list.append((x, "${0:.2f}".format(my_dictionary[x])))
    return my_list


# print(calculate_expenses("expenses.txt"))
