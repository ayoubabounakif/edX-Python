# Function that accepts two positive integers which are the height and width
# of a rectangle and returns a list that contains the area and perimeter of that rectangle

# CODE

def aap_of_rectangle(height, width):
    area = width * height
    perimeter = (height + width) * 2
    x = [area, perimeter]
    return x
