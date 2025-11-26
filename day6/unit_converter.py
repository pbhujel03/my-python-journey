def km_to_miles(km):
    return km*0.621371

def miles_to_km(miles):
    return miles/0.621371

def celcius_to_fahrenheit(c):
    return (c*9/5)+32

def fahrenheit_to_celcius(f):
    return (f-32)* 5/9

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(lb):
    return lb/2.20462

def show_menu():
    print("Unit Converter Menu:")
    print("1. km to miles")
    print("2. miles to km")
    print("3. celcius to fahrenheit")
    print("4. fahrenheit to celcius")
    print("5. kg to lb")
    print("6.lb to kg")
    print("7. exit")

while True:
    show_menu()
    choice = input("Enter your choice(1-7):")

    if choice == "1":
        km = float(input("Enter Kilometers: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles ")

    elif choice == "2":
        miles = float(input("Enter Miles:"))
        print(f"{miles} miles = {miles_to_km(miles):.2f} km")

    elif choice == "3":
        c= float(input("Enter the temperature in celcius:"))
        print(f"{c} c = {celcius_to_fahrenheit(c):.2f} F")

    elif choice == "4":
        f= float(input("Enter the temperature in Fahrenheit:"))
        print(f"{f} f = {fahrenheit_to_celcius(f):.2f} C")

    elif choice == "5":
        kg= float(input("Enter the Kilograms:"))
        print(f"{kg} kg = {kg_to_pounds(kg):.2f} lb")
    
    elif choice == "6":
        lb = float(input("Enter the pounds:"))
        print(f"{lb} lb = {pounds_to_kg(lb):.2f} kg")

    elif choice =="7":
        print("exiting")
        break

    else:
        print("Invalid Choice.")
