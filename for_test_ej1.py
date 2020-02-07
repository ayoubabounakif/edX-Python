"""1minute = 60s
1hr = 60*60 =  3600s
1d = 60 * 60 * 24 = 86400s"""

ask_user = input("Enter the number of secs \
		that you want to convert to usual time")

time = int(ask_user)
if time < 0:
	break

if time <= 0:
	days = time // 86400
	hours = (time - (days * 86400)) // 3600
	minuts = (time - ((days * 86400)) + (hours * 3600)) // 60
	seconds = (time - ((days * 86400) + (hours * 3600) + (minuts * 60))) // 1

x = print (days, hours, minuts, seconds)
print (x)

if x is true:
	print ("There is nothing else to convert, rerun the program")
