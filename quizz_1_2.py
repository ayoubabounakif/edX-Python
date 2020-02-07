
#search for a better algorithm and use a list
#week_days = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]

ask_user = input("Positive integer between 1 and 7:")

number = int(ask_user)


if number == 1:
    print ("MONDAY")

elif number == 2:
    print ("TUESDAY")

elif number == 3:
    print("WEDNESDAY")

elif number == 4:
    print("THURSDAY")

elif number == 5:
    print("FRIDAY")

elif number == 6:
    print("SATURDAY")

elif number == 7:
    print ("SUNDAY")

else:
    print ("ERROR! Enter an integer between 1 and 7")


