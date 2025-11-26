pocket_money = float(input("Enter Your Pocket Money:"))

expenses_list = []

while True:
    expenses = float(input("enter your expenses:"))
    expenses_list.append(expenses) #add the expenses to the expenses list

    total_expenses = sum(expenses_list)
    left_money = round(pocket_money-total_expenses,2)

    more_expenses = input("do you want to add another expenses?")
    if more_expenses.lower() !='yes':
        break

    
print ("you have Rs", left_money,"left, spend wisely")
