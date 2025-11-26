age = int(input("Enter Your age:"))

is_student = input("Are you a student? (yes/no)").lower()

ticket_price = 300

if age <= 18 and is_student=="yes":
    discount = 0.5
    final_price = ticket_price*(1-discount)
    print("you will get the 50% student discount")

elif is_student =="yes":
    discount = 0.3
    final_price = ticket_price*(1-discount)
    print("You will get a 30 % discount")

else:
    final_price = ticket_price
    print("No discount")

print(f"your final ticket price is {round(final_price,2)}")

