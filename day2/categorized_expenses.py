pocket_money = float(input("enter Your pocket money:"))

expenses_dict = {}
while True:
    expenses = float(input("Enter Your expenses:"))
    category = input("enter Your category:")

    if category in expenses_dict:
        expenses_dict[category].append(expenses)
    
    else:
        expenses_dict[category]=[expenses]

    total_expenses = sum(sum(expenses) for expenses in expenses_dict.values())
    remaining_balance = round(pocket_money-total_expenses,2) 

    print("you have Rs",remaining_balance,"left")

    more_expenses = input("Do you want to dd another expenses? ")
    if more_expenses.lower()!='yes':
        break
print ("expenses summary:")
for category, expenses in expenses_dict.items():
    category_total = sum(expenses)
    print(f"{category}: Rs {category_total}")

print(f"Remaining balance: Rs {remaining_balance}")

