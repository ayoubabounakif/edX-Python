def nums_to_words(integer):
    string = str(integer)
    string = list(string)
    output_str = ""
    dictionary = {"1" : "one",
                  "2" : "two",
                  "3" : "three",
                  "4" : "four",
                  "5" : "five",
                  "6" : "six",
                  "7" : "seven",
                  "8" : "eight",
                  "9" : "nine",
                  "0" : "zero"}
    for i in string:
        output_str = output_str + dictionary[i] +  " "
        strip = output_str.strip()
    return strip

print (nums_to_words(4300))
