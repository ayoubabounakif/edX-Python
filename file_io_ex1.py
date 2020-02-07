def list_from_file(file_name):
    output_list = []
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        output_list.append(line.strip('\n'))
    return output_list

def dict_from_file(file_name):
    output_dict = {}
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        name, course1, course2, course3, course4 = line.strip().split(',')
        output_dict[name] = [float(course1), float(course2), float(course3), float(course4)]
    return output_dict

def dict_from_file_2(file_name):
    output_dict = {}
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        # Skip any lines start with #
        if line[0] != '#':
            name, math, physics, chemistry, biology = line.strip().split(',')
            if float(math) > 70 and float(chemistry) > 70:
                output_dict[name] = [float(math), float(physics), float(chemistry), float(biology)]
    return output_dict

def dict_from_file_3(file_name):
    output_dict = {}
    output_dict["milk"] = []
    output_dict["bread"] = []
    # Make a connection to the file
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        first_character = line[0]
        # Remove the first first_character &
        # strip and split by white space
        items = line[1::].strip().split()
        # Change the string items into floats
        # the line below is an example of doing it by list comprehensions
        # float_items = [float(x) for x in items]
        float_items = []
        for current_item in items:
            float_items.append(float(current_item))
        if first_character == "m":
            output_dict["milk"] += [float_items]
        if first_character == "b":
            output_dict["bread"] += [float_items]
    return output_dict

def nested_dict_from_file(file_name):
    output_dict = {}
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line[0] != '#':
            # Split the line with the delimiter comma ('.')
            first_name, last_name, age = line.strip().split(',')
            if last_name not in output_dict:
                output_dict[last_name] = {first_name : int(age)}
            elif first_name not in output_dict[last_name]:
                output_dict[last_name][first_name] = int(age)
    return output_dict

"""def _construct_nested_dictionary_from_file_sample_(filename):
    my_dictionary = {}
    # set the mode to read mode
    mode = "r"
    # Make a connection to the file
    file_pointer = open(filename, mode)
    data = file_pointer.readlines()
    for line in data:
        if line[0] != "#":
            # Split the line with the delimiter comma (',')
            first_name, last_name, age = line.strip().split(',')
            if last_name not in my_dictionary:
                my_dictionary[last_name] = {first_name: int(age)}
            else:
                if first_name not in my_dictionary[last_name]:
                    my_dictionary[last_name][first_name] = int(age)
    return my_dictionary"""
