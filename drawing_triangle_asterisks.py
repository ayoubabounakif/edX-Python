ask_user = int(input("Type an integer:"))
for i in range (1, ask_user+1):
    for j in range (1, i+1):
        print ('*', end='')
    print ()
    
for i in range(ask_user-1, 0, -1):
    for j in range(0, i):
        print ('*', end='')
    print()
