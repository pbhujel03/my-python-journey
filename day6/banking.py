balance = 0
transaction_history = []

try:
    with open("pin.txt","r") as f:
        pin = f.read().strip()
except FileNotFoundError:
    pin="1234"

def deposit(amount):
    global balance
    if amount>0:
        balance+=amount
        transaction_history.append(f"Rs{amount:.2f} deposited successfully.")
    else:
        print("Deposit amount must be greater than 0.")

def withdraw(amount):
    global balance 
    if amount<=0:
        transaction_history.append("Withdrawal Amount must be greater than 0")
    elif amount>balance:
        transaction_history.append("insufficient Balance")
    else:
        balance-=amount
        transaction_history.append(f"Rs {amount:.2f} withdrawn successfully.")
    
def check_balance():
    global balance
    print(f"Your Current balance is: Rs{balance:.2f}")

def cal_interest(rate, years):
    global balance
    interest = balance * (rate/100) * years
    balance += interest
    transaction_history.append(f"Interest Earned over {years} years:Rs {interest:.2f}")
    print(f"Rs{interest: .2f} interest added to your balance.")

def calculate_compound_interest(p,r,n,t):
    A=p*(1+r/n)**(n*t)
    return A

def use_compound_interest():
    try:
        p= float(input("Enter the principal amount (Rs):"))
        r = float(input("Enter the annual interest rate (%):"))/100
        n = int(input("Time interest is compounded per year:"))
        t = float( input("Number of Years"))

        A=calculate_compound_interest(p,r,n,t)
        interest = A-p
        print(f"Final amount after{t} years: Rs {A:.2f}")
        print(f"total compound interest earned : Rs{interest:.2f}")
        transaction_history.append(f"Compound Interest: Rs {interest:.2f} on Rs {p:.2f} for {t} years")
    except ValueError:
        print("Invalid input")

def change_pin():
    global pin
    current = input("Enter Your Current pin:")
    if current == pin :
        new_pin = input("Enter New Pin:")
        confirm = input("Congirm your new pin:")

        if new_pin == confirm :
            pin = new_pin
            with open ("pin.txt","w")as f:
                f.write(pin)
            print("Pin changed successfully")
        else:
            print("Pin didn't match")
    else:
        print("Incorrect Pin.")

def export_account_summary():
    filename = "account_summary.txt"

    try:
        with open(filename,"w") as f:
            f.write("Account Summary")
            f.write(f"Current Balance is: Rs{balance:.2f}\n\n")
            f.write("Transaction History:\n")

            if not transaction_history:
                f.write("no transaction Yet")
            else:
                for entry in transaction_history:
                    f.write(f"-{entry}\n")

        print("Account Summary Exported Successfully. to '{filename}'.")

    except Exception as e:
        print(f"Error exporting account summary:{e}")


def bank_operations():
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. calculate interest")
    print("5. Show Transaction History")
    print("6. Change pin")
    print("7.Compound Interest Calculator")
    print("8. Export Account Summary to File")
    print("9. Exit")
   
#    pin protection
attempts = 3
while attempts > 0:
    entered_pin = input ("Enter 4 Digit Pin:")
    if entered_pin == pin :
        print("Access Granted.")
        break
    else:
        attempts -= 1
        print(f"Incorrect Pin. Attempts left: {attempts}")

if attempts == 0:
    print("Too many attempts. Access Denied.")

else:
    while True:
        bank_operations()
        choice = input("Choose an operation(1-9):")
        if choice =="1":
            try:
                amount = float(input("Enter the amount to deposit: Rs "))
                deposit(amount)
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == "2":
            try:
                amount = float(input("enter the amount to withdraw: Rs"))
                withdraw(amount)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "3":
            check_balance()

        elif choice =="4":
            try:
                rate = float(input("Enter the Rate:"))
                years = int(input("Enter the Time:"))
                cal_interest(rate, years)
            except ValueError:
                print("Invalid input! Please enter a number.")

        elif choice == "5":
            print("\n Transaction History:")

            if not transaction_history:
                print("No Transaction yet")
            else:
                for entry in transaction_history:
                    print("-",entry)     

        elif choice == "6" :
            change_pin()  
        
        elif choice == "7":
            use_compound_interest()
        
        elif choice == "8":
            export_account_summary()

        elif choice == "9":
            print("\n📄 Final Transaction History:")
            if not transaction_history:
                print("No transactions were made.")
            else:
                for entry in transaction_history:
                    print("-", entry)
            print("👋 Exiting the app. Thank you!")
            break
        else:
            print("Invalid Choice.")
