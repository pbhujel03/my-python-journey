

age = int(input("Enter Your age:"))

is_student = input("Are you a student?(yes/no)").lower()

movie_time = input("Enter movie time:").lower()

ticket_price = 300

if age<12:
    ticket_price = 100
    print("you are a child, ticket Rs 100")

elif age>60:
    discount = 0.4
    ticket_price*=(1-discount)
    print("40% discount Applied because you are senior")

elif age>12 and age <60:
    if is_student == "yes":
        discount = 0.5
        ticket_price *=(1-discount)
        print("You are a student, 50% discount applied")
    else:
        discount = 0.3
        ticket_price *= (1-discount)
        print("30% discount applied")

else:
    print("You are a adult so, no discount")

if movie_time == "matinee":
    ticket_price-=50
    print("you selected a matine show, Rs 50 discount applied.")

print(f"Your final price is Rs{ round(ticket_price,2)}")



