import datetime
import random

motivations = ["raat","paxi","aauxa","sadhai","Din","jasari"]

today=datetime.date.today()
selected_quote=random.choice(motivations)

formatted_date=today.strftime("%B %d,%Y")


print("Daily Motivations")
print(f"Today's Motivation for {formatted_date} is:") 
# //with f

print(selected_quote)

file= open("motivations.txt","a")

file.write(f"{formatted_date}-{selected_quote}\n")

file.close()

