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
    file_pointer = open(file_name, 'r')
    data = file_pointer.readlines()
    for line in data:
        if line[0] == "m":
            m, price1, price2, price3 = line.strip().split(',')
            output_dict["milk"] = [float(price1), float(price2), float(price3)]
        if line[0] == "b":
            b, price1, price2, price3 = line.strip().split(',')
            output_dict["bread"] = [float(price1), float(price2), float(price3)]
    return output_dict
