# Width and Precision comprehension
my_course = [["Buny", 100, 87, 95], ["Duck", 78, 9, 89], ["Rubb", 83, 85, 92]]
for student in my_course:
    for item in student:
        if type(item) == str:
            print("{0:5s} | ".format(item), end="")
        else:
            print("{0:3d} | ".format(item), end="")
    print("")

my_string = "x = {0:%<7d} and y = {1:@>8d}".format(5, 43)
print(my_string)

my_string = "x = {0:#^7d} and y = {1:@>8.4f}".format(6, 0.2)
print(my_string)

my_string = "x = {0:*^7s} and y = {1:?<8.2f}".format("cat", 4.256)
print(my_string)

a = "john"
b = "happy"
my_string = "{0:*^10} is {1:+^9s}".format(a, b)
print(my_string)

# a = "mary"
# b = "fine"
# my_string = "{0:5s} is {1:5s} and {}".format(a, b)
# print(my_string)"""

my_string = "x = {1:*>6.4f} and y = {1:+5.3f}".format(2.3, -4.12345678)
print(my_string)


# my_string = "x = {1:*3d} and y = {0:-4.2f}".format(5, -0.5)
# print(my_string)

my_string = "x = {0:+4.2f} and y = {1:+5.3f}".format(3.45, -2.23)
print(my_string)

my_string = "x = {0:-3.1f} and y = {1:+3.2f}".format(2.44, -3.76)
print(my_string)

my_string = "x = {0: 3d} and y = {1:+4d}".format(223, -45)
print(my_string)

print('X{0:Y<7d}Z'.format(123))
print('X{0:Y^9}Z'.format('dog'))
print('A{1:C>10.3f}B'.format(12.56, 356.1234))
print("A{0:x<8.2f}B".format(12.1234567))
print("A{0:x^9.2f}B".format(97.234321))

print('A{0:0.0f}B'.format(7.89))
print('A{0:C>7d}B'.format(5432))
print('A{0:Z^8}B'.format('bird'))
print('A{1:}y{0:}B'.format('x', 'y', 'z'))
print('A{0:C<7d}B'.format(5432))

print('A{0:,}B'.format(12345678))
# print('A{1:6}B'.format(12))
print('A{0:C<8.2f}B'.format(12.345678))
print('A{0:1.3f}B'.format(12.56789))
print('{0:#>6d}'.format(25))

print('{0:0.2f}'.format(12.12345))
print('x{2:}y{1:}z'.format('A', 'B', 'C'))
print('x{0:z<10.3f}y'.format(987.654321))
print('x{1:z^5}y'.format('one', 'two'))
print('x{0:z^-6d}y'.format(5432))

print('x{0:z>6d}y'.format(5432))
print('x{0:z^8d}Y'.format(5432))
print('x{0:0.0f}y'.format(2.6789))
print('AA{0:+5.3f}BB'.format(123.456789))
print('AA{0:C<7}BB'.format(987))

print("{1}AA{0}{1}BB" .format("dog", "cat", 4))
# print('xx{1:B>5}YY'.format(23))
print('xx{0:C<+7}yy'.format(+23))
print("AA{1:x^5}BB".format(123, "dog"))
print("{2}{1}" .format("pet", 2.45, "cat"))
