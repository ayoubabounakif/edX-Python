def find_n_letter_words(string, n):
    words = string.split()
    #print (words)
    iteration = 0
    for x in words:
        if len(x) == n:
            #print (x)
            iteration = iteration + 1

    return iteration

test_string = "Python is an interpreted high-level programming language \
for general-purpose programming. Created by Guido van Rossum \
and first released in 1991, \
Python has a design philosophy that emphasizes code readability\
notably using significant whitespace. \
It provides constructs that enable clear programming on both small and large scales."
total_words = 0
for k in range(1, 11):
    output = find_n_letter_words(test_string, k)
    total_words = total_words + output
    print ("There are", output,"words with", k,"characters.")

print ("****\nThere are", total_words, "words in this string")
