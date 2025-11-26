loan_amt = float(input("Enter Your Loan Amount(Principal)"))
interest = float(input("Enter Your interest Rate)"))
time = float(input("enter the loan duration(in years)"))

monthly_interest = interest/100/12
monthly_time = time*12

if monthly_interest ==0:
    monthly_payment = loan_amt/monthly_time

else:
    monthly_payment = loan_amt*monthly_interest* (1+monthly_interest)**monthly_time/ ((1+monthly_interest)**monthly_time-1)

total_payment = monthly_payment * monthly_time
total_interest = total_payment - loan_amt
 
print(f"monthly Payment : Rs{round(monthly_payment,2)}")
print(f"Total Payment over {time} years: Rs {round(total_payment,2)}")
print(f"Total Interest Paid: Rs {round(total_interest,2)}")