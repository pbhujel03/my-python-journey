import datetime

birth_year = int(input("Enter Your Birth year:"))
birth_month = int(input("Enter Your Birth Month(1-12):"))
birth_day = int(input("Enter Your Birth day:"))

birth_date = datetime.date(birth_year,birth_month,birth_day)

present_day = datetime.date.today()

total_age = (present_day-birth_date).days

age_years = total_age//365
remaining_days = total_age%365
age_months = remaining_days // 30
age_days = remaining_days % 30

print(f"your Full Age is:{age_years} years, {age_months} months, and {age_days} days old")