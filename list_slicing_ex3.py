# Function that accepts a list as input and returns a new list
# which includes every other element in the original list.
# Keep the first element i.e input_list[0]
# input_list = ["we", "love", "python", "so","much"]
# ['we', 'python','much']

# CODE

def test(x):
    new_list = []
    length = len(x)
    new_list.append(x[0])
    for element in range(1, length):
        if element % 2 == 0:
            new_list.append(x[element])
    return new_list

print (test(["we", "love", "python", "so","much"]))
    
    
