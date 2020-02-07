def count_char(string, char):
    count = 0
    for x in string.lower():
        if x == char.lower():
            count = count + 1
    return count
