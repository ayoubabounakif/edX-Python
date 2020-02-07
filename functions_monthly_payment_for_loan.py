def monthly_loan(principal, annual_interest_rate, duration): # Function w 3 arguments
    r = (annual_interest_rate / 100) / 12 # Define r
    n = (duration * 12) # Define n
    
    if r == 0: # Check if r equals 0
        monthly_payment = principal / n # If it is, do the following 
        
    else: # If r is something else
        monthly_payment = (principal * (r*(1+r)**n) / float((1+r)**n - 1)) # Do that 
        
    return monthly_payment # Return monthly_payment

print (monthly_loan(1000.0, 4.5, 5)) # Test 

