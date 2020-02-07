# Program that displays the loan information

# Function for calculating payment
def monthly_loan(principal, annual_interest_rate, duration):
    r = (annual_interest_rate / 100) / 12
    n = (duration * 12)
    if r == 0:
        monthly_payment = principal / n
    else:
        monthly_payment = (principal * (r*(1+r)**n) / float((1+r)**n - 1))
    return (monthly_payment)

# Function for calculating remaining balance
def remaining_loan(principal, annual_interest_rate, duration , number_of_payments):
    r = (annual_interest_rate / 100) / 12
    n = (duration * 12)
    p = number_of_payments
    if r == 0:
        remaining_loan_balance = principal * (1-(p/n))
    else:
        remaining_loan_balance = principal * ((1.0+r)**n - (1.0+r)**p) / (((1+r)**n)-1)
    return (remaining_loan_balance)

# Main Program
principal = float(input("Enter loan amount: "))
annual_interest_rate = float(input("Enter annual interest rate (percent): "))
duration = int(input("Enter loan duration in years: "))
monthly_payment = monthly_loan(principal, annual_interest_rate, duration)

print ("LOAN AMOUNT:",int((principal)),"INTEREST RATE (PERCENT):",int(annual_interest_rate))
print ("DURATION (YEARS):",duration,"MONTHLY PAYMENT:",int(monthly_loan(int((principal)), int(annual_interest_rate), duration)))
for year_number in range (1,1+duration):
    y = remaining_loan(principal, annual_interest_rate, duration, year_number * 12)
    print ('YEAR:',year_number, 'BALANCE:', int(y), 'TOTAL PAYMENT', int(monthly_payment * year_number * 12))













