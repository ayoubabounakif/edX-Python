def list_of_primes(n):
    output_list = []
    for i in range(2, n):
        #print (i)
        isPrime = True
        for num in range(2, i):
            #print (num)
            if i % num == 0:
                print (i%num)
                isPrime = False
        if isPrime:
                output_list.append(i)
            #print (output_list)
                output_list.sort()
    return output_list

def test(n):
    output_list = []
    for i in range(2, n):
        for number in range(2, i):
            if i % number == 0:
                break
        else:
            output_list.append(i)
            output_list.sort()
    return output_list

print (test(10))
