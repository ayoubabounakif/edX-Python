def vowels_count(string):
    result = 0
    string = string.lower()
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in string:
        if i in vowels:
            result = result + 1

    return result

