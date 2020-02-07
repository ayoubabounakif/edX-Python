###### MY CODE ######
def count_consonants(string):
    alphabet = 'bcdfghjklmnpqrstvwxyz'
    count = 0
    for char in string.lower():
        if char in alphabet:
            count = count + 1
    return count

###### INSTRUCTOR CODE ######
def total_consonants_sample(sample_string):
    spaces_removed = sample_string.replace(" ", "")
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for char in spaces_removed.lower():
        if char not in vowels:
            count = count + 1
    return count
