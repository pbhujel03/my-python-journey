import datetime
import random

motivations = ["raat","paxi","aauxa","sadhai","Din","jasari"]

today=datetime.date.today()
selected_quote=random.choice(motivations)

# formatted_date=today.strftime("%B %d,%Y")
formatted_date=today.strftime("%Y/%m/%d")

print("Daily Motivations")
print(f"Today's Motivation for {formatted_date} is:") 
# //with f

print("Today's Motivation for"+ formatted_date+" is:") 
# // without f
print(selected_quote)











