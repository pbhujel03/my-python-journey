pocket_money = float(input("Enter Your Pocket Money:"))
expenses = float(input("Enter Your Total expenses:"))

# money_left = pocket_money - expenses
money_left = round(pocket_money - expenses,3)

print("you have",money_left, "Money Left. spend properly ")