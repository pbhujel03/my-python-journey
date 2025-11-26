import datetime

birthyear = int(input("Enter Your Birth Year:"))

present_year = datetime.datetime.now().year

age = (present_year-birthyear)

print(f"your Age is",age)
