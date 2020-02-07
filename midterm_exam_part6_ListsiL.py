###### MY CODE ######

def palindrome(x):
    return x == x[::-1]

###### INSTRUCTOR CODE ######
def test_list_palindrom_edx(some_list):
    size = len(some_list)
    if size % 2 == 0:
        # if the length is even
        mid = int(size / 2)
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid::][::-1]
    else:
        mid = int((size ) / 2)
        # get the first half
        first_half = some_list[0:mid]
        # get the second half and reverse it
        second_half = some_list[mid+1::][::-1]
    if first_half == second_half:
        return True
    else:
        return False


