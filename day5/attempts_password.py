import getpass
attempts = 0

while True:
    password = getpass.getpass("Enter Your Password:")
    confirm_pass = getpass.getpass("Enter Password")

    attempts+=1

    if password != confirm_pass:
        print("try again")
        continue

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@#$%^&*()-_=+<>/?\\|{}[]~"

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_characters:
            has_special = True
    
    if len(password) < 8:
        print("PW must be at least 8 characters long.")
    if not has_upper:
        print("PW must include at least one uppercase letter.")
    if not has_lower:
        print("PW must include at least one lowercase letter.")
    if not has_digit:
        print("PW must have at least one digit")
    if not has_special:
        print("PW must have at least one special character.")

    if (len(password)>= 8 and has_upper and has_lower and has_digit and has_special):
        print("Strong PW Accepted!")
        
        print(f" it took you {attempts} attrmpts to enter a stro0ng password.")

        with open("saved.txt","w") as f:
            f.write(password)
            print("Password Saved")
        break

    else:
        
        print("Try again!!")
   