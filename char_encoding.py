def int_to_char(a):
    char = chr(a)
    return char


def char_to_int(b):
    int = ord(b)
    return int


def encoding (x, y):
    encoding = ""
    for i in range (x, y+1):
        encoding = encoding + chr(i)
    return encoding

print (encoding(2000,20000))

######## Sum of Character Code Values ########
def sum_ccv(s):
    sum = 0
    for char in map(ord, s):
        sum += char
    return sum
