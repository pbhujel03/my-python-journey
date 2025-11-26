import getpass


while True:
    # password = input("Enter Your Password:")
    # password = getpass.getpass("Enter Your Password:")
    password = getpass.getpass("Enter Your Password:")
    confirm_password = getpass.getpass("Enter Password")


    if password != confirm_password:
        print("PW do not match, please try again.")
        continue


    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+<>/?\\|{}[]~"

    for char in password:
        if char.isupper():
            has_upper=True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
        
        strength_score = 0

    if len(password)>=8:
        strength_score+=1
    if has_upper:
        strength_score+=1
    if has_lower:
        strength_score+=1
    if has_digit:
        strength_score +=1
    if has_special:
        strength_score +=1
    

    if strength_score <=2:
        print("Weak Password!!")
    elif strength_score == 3 or strength_score ==4:
        print("Medium Password")
    else:
        print("Strong Password")

    with open("saved_password.txt","w") as f:
        f.write(password)
    print("Password Saved")

    # choice = input("Do you want to try another Password ? (yes/No):").lower()
    # if choice != "yes":
    #     print("Goodbye!!")
    break
    