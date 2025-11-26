bill_amt = float(input("Enter Your Bill amount:"))
tip_percent = float(input("Enter the tip Percentage you want to give "))

tip_amt = (tip_percent/100)*bill_amt
total_amt = bill_amt+tip_amt

print(f"Tip amount : Rs{round(tip_amt, 2)}")
print(f"Total bill amount : Rs {round(total_amt, 2)}")

split = input("Do you want to split?").lower()

if split == "yes":
    people = int(input("Enter the number of people:"))

    amt_per_person = total_amt/people

    print(f"Each Person should pay :Rs {round(amt_per_person,2)}")

    