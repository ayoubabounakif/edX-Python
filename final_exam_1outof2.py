my_list = [[2,3],[6,5],[10,9]]
print(my_list[0:2])

my_list = []
for m in range(0,2):
    new_list = []
    for k in range(2,4):
        new_list.append(k)
    my_list.append(new_list)
print(my_list)

my_list = []
for k in range(1,101,10):
    my_list.append(k)
print (my_list[: :3])

my_list = [2, 3, 4]
for k in range(3):
    my_list.insert(-k, k+1)
print(my_list)

def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [2,4,3]
my_fun(m)
print(m)

def my_fun(a):
    a[0] = 'new name'
    a[1] = 'john'
x = ['old name', 'jack']
my_fun(x)
print (x)

my_list = [[3,2],[2,6,4]]
x = 0
new_list=[]
for m in range(len(my_list)):
    for k in range(len(my_list[m])):
        x =  my_list[m][k]
        new_list.append(x)
print(new_list)

m = 0
my_str_1 = "car"
my_str_2 = "cat"
for char_1 in my_str_1:
    for char_2 in my_str_2:
        if char_1 != char_2:
            m = m + 1
print([m])

x = "bye bob"
print ([x.strip("b")])

m = 0
for x in range (4,6):
   for y in range (2,4):
      m = m + x + y
print ([m])

x = "mississipi"
print (x.replace('i','z',2))

x = ["duck", "car", "pet"]
print ("AA".join(x))

k = 10
while k > 2:
    x = k / 3
    k = k - 1
print(x)

numbers={"one": [1,"uno"], "two": [2,"dos"]}
print (numbers["one"][1][2])

"""
# Prints out an error
d={1:"one", "two": 2 , 3: "tres"}
# print (d["tres"])

"""

my_string = "x = {0:#^7d} and y = {1:@>8.3f}".format(5, 0.3)
print (my_string)

print('A{0:B^9}C'.format('dog'))

def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z
y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print (my_fun(y))


list_1 = ["cat", 3, "cat" , 25, 12]
list_2 = ["car", 25, "dog" , 43]
count = 0
for item in list_1:
    if item in list_2:
        count = count + 1
print (count)

print('{0:,}'.format(12345678))
