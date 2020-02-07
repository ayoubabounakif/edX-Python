def ret_even_numbers(test_list):
    even_numbers = []                   # Create an empty list

    for i in test_list:                 # Iterate through the input list
        if i % 2 == 0:                  # Check if number is even
            even_numbers.append(i)      # If it is, store it
            
    return even_numbers                 # Return the list of even numbers

