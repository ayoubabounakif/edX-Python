def test_for_anagrams(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()
    if sorted(str_1) == sorted(str_2):
        return True
    else:
        return False


print (test_for_anagrams('Orchestra', 'Carthorse'))
print (test_for_anagrams('pupil', 'tuple'))
print (test_for_anagrams('protectional', 'lactoprotein'))
print (test_for_anagrams('Angered', 'enraged'))
