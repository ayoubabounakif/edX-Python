x = ["dog", 2, "cat", 34, 5.8]
m = 0
for i in range(len(x)):
    m = m + i
print(m)


def my_fun(x,y):
    m = x ** y  
y = my_fun(2, 3)    
print(y)


i = 1
while False:
    if i % 5 == 0:
        break
    i = i + 2
print(i)


count = 0
list_1 = []
for i in range(1,4):
    list_1.append(i**2)
for x in list_1:
    count = count + x
print(count)


def my_fun(a):
    a[0] = 'new value:'     
    a[1] = a[1] + 1      

x = ['old value:', 99]
my_fun(x)
print (x[0], x[1])


x = [ 2, "dog", 6, 4, "pet", 3, 9, "cat"]
count = 0
for item in x:
    m = 0
    if item == "pet" or item == 3:
        m = x.index(item)
        count = count + m
print(count)


count = 0
my_list = [2, 4, 1, 5, 7, 3, 9, 4]
new_list = my_list[1:7:2]
for item in new_list:
    count = count + 1
print(count)


x = 0
my_list = []
while x < 10:
    if x % 2 == 0:
        my_list.append("dog")
    elif x % 3 == 0:
        my_list.remove("dog")
    x = x + 1
print(my_list.count("dog"))


list_1 = ["dog", 3, "cat" , 25, 2.4]
list_2 = ["car", 25, "dog" , 43]
count = 0
for item in list_1:
    if item in list_2:
        count = count + 1
print (count)


def my_fun(x):
    z = 0
    for item in x:
        m = x.count(item)
        if m > z:
            z = m
    return z

y = ["cat", 4, "dog" , "cat" , 2, "cat", 2]
print (my_fun(y))


my_list = []
for k in range(1,101,20):
    my_list.append(k)
print (my_list[: :2])


def my_fun(x):
    for k in range (len(x)):
        x.extend(x[:k])
m = [1,5,3]
my_fun(m)
print(m)

def my_fun(x):
    for k in range (len(x)):
        x.append(x[:k])
m = [1,5,3]
my_fun(m)
print(m)


####### (Work this code again)
my_list = [9, 8, 7]
for k in range (3):
    my_list.insert(-k, k+1)
print(my_list)
####### (Work this code again)


####### (Work this code again)
my_list = [12, "cat", 3.4, "dog", 62]
new_list = []
for k in range(5):
    if k % 2:
        m = my_list.pop(k)
        new_list.append(m)
print(new_list)
####### (Work this code again)


def my_fun(my_list,s,e):
    del (my_list[s:e])
 
values = [2, 9, 16, 3, 24, 13, 15]
my_fun(values,-6,-4)
my_fun(values,2,4)
print(values)


def my_fun(i):
    values = []
    values.append(i)
    return values
my_fun(5)
print(my_fun(3))


def my_fun(m):
    x = []
    for k in range(len(m)):
        if m[k] % 3 == 0 and m[k] % 2:
            x.insert(k, m[k])
    return x
 
values = [2, 9, 16, 3, 24, 13, 15]
print(my_fun(values))


def my_fun(m, increment):
    x = 0
    while x < len(m):
        m[x] = m[x] + increment
        x = x + 1
    return m 

values = [4, 3, 7]
print(my_fun(values, 2))


def my_fun(m):
    x = m[:]
    for k in x:
        if type(k) == int:
            m.remove(k)

values = [3, [3,4], 2.9, 3, 6, 'dog', 5]
my_fun(values)
print(values)





















