#program which prints the sum of all the even numbers from 1 to 101.

i = 1
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum = sum + i
print (sum)
