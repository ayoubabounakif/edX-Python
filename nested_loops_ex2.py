m = 0
x = 1
while x < 4:
    y = 1
    while y < 3:
        m = m + x + y
        y = y + 1
    x = x + 1
#print(m)

m = 0
x = 1
while x < 4:
    y = 1
    while y < 5:   
        m = m + y
        y = y + 1
        if x + y == 5:
            break
    x = x + 1
#print (m)

m = 0
x = 10
while x > 8:
    for y in range(1,3):
        m = m + 1
    x = x - 1
#print(m)
