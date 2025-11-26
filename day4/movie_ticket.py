age = int(input("Enter your age:"))

is_student = input("Are you a student?(yes/No)")

if age<18 or is_student.lower()=="yes":
    print("you are eligible for a student discount")

else:
    print("you need to pay the full price.")


    