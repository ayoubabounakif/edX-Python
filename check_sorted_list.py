def sorted_list(list):
    copy_list = list[:]
    list.sort()
    if list == copy_list:
        return True
    else:
        return False

