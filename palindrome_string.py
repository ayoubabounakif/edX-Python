def pal_test(string):
    if str(string).lower() == str(string)[::-1].lower():
        return True
    else:
        return False
