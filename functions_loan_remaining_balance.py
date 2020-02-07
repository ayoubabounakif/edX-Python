# Program that calculate the remaining balance of a loan

def remaining_loan(principal, annual_interest_rate, duration , number_of_payments):
    r = (annual_interest_rate / 100) / 12
    n = (duration * 12)
    p = number_of_payments
    
    if r == 0:
        remaining_loan_balance = principal * (1-(p/n))
    else:
        remaining_loan_balance = principal * ((1.0+r)**n - (1.0+r)**p) / (((1+r)**n)-1)
    return remaining_loan_balance

print (remaining_loan(1000.0, 4.5, 5, 12))


