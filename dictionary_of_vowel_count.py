def vowel_count_dict(string):
    string = string.replace(" ", "")
    string = string.lower()
    output_dict = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in string:
        if x in vowels:
            output_dict[x] = string.count(x)
    return output_dict

print (vowel_count_dict('Hardcozyzmpooooaaaoooioooooded'))
