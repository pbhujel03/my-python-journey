# goals = float(input("Enter Your Goal Amount:"))

# money =[]
# while True:
#     saved_money= float(input("enter Your Saved Amount:"))
#     money.append(saved_money)

#     total_saved = sum(money)

#     remaining_amount = round(goals-total_saved,2)
#     more_money = input("Do you have more money?")
#     if more_money.lower() != "yes":
#         break
    
# print(f"you need to save {remaining_amount} to reach your goal {goals}")

goal_amt = float(input("Enter your savings Goal Amount:"))

current_savings = 0
while current_savings<goal_amt:
    contribution = float(input("Enter Your Contribution:"))
    current_savings += contribution

    remaining_amt = goal_amt- current_savings

    if remaining_amt>0:
        print(f"Great Job! You have saved {current_savings}. you still need {remaining_amt} to reach your goal")

    else:
        print("congratulations:")

    more_contributions = input("Do you want to add more Contributions?")
    if more_contributions.lower()!= "yes":
        break