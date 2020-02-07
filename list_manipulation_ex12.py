# Program that asks the user to enter an integer between 1 and 9999
# (both inclusive) and then prints the input integer using words.
# For example if the user enters: ---> 3421
# Then your program should print ---> three thousand four hundred twenty one

#################### MY CODE ####################

user = int(input("Please enter an integer between 1 and 9999: "))
one_ten=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten_nineteen=['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
'sixteen', 'seventeen', 'eighteen', 'nineteen']
twenty_ninety=[' ', ' ','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty',
'ninety']
temp_str = ""

if user == 0:
    temp_str = 'zero '
    # print ('zero')

first_digit = user // 1000
second_digit = (user % 1000) // 100
third_digit = (user % 100) // 10
fourth_digit = (user % 10)

if first_digit > 0:
    temp_str = temp_str + one_ten[first_digit] + ' thousand '
    # print (one_ten[first_digit],'thousand ',end = '')

if second_digit > 0:
    temp_str = temp_str + one_ten[second_digit] + ' hundred '
    # print (one_ten[second_digit],'hundred ',end = '')

if third_digit > 1:
    temp_str = temp_str + twenty_ninety[third_digit] + " "
    # print (twenty_ninety[third_digit],'',end = '')

if third_digit == 1:
    temp_str = temp_str + ten_nineteen[fourth_digit] + " "
    # print (ten_nineteen [fourth_digit],'',end = '')

else:
    if fourth_digit:
        temp_str = temp_str + one_ten[fourth_digit] + " "
        # print (one_ten[fourth_digit],'',end = '')

if temp_str[-1] == " ":
    temp_str = temp_str[0:-1]

print (temp_str)
