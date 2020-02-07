numbers={"one": 1, "two": 2, "three": 3}
print (numbers["two"])

numbers={"one": "uno", "two": "dos"}
numbers["dos"]="two"
print (numbers["two"])

numbers={"one": 1, "two": [4, 6, 3], "three": 3}
x = (numbers["two"])
x.sort()
print(x)

numbers={"one": "uno", "two": "dos", "three": "tres"}
print ("uno"  in numbers)

numbers={"one": "uno", "two": "dos", "three": "tres"}
print ("two" in numbers)

numbers={"one": "uno", "two": "dos", "three": "tres"}
print (numbers["three"])

numbers={"one": "uno", "two": "dos"}
numbers["two"]=1
print (numbers["dos"]) # ERROR

numbers={"one": 1, "two": 2}
print (numbers[2]) # ERROR
