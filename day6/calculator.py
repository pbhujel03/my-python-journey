def calculate_tatal(price, quantity):
    return price*quantity

num_items = int(input("How many different grocery items are you buying?"))

grand_total = 0

for i in range(num_items):
    print(f"items {i+1}")
    price = float(input("Enter the price per unit : Rs "))
    quantity = float(input("Enter the quantity:"))

    item_total = calculate_tatal(price,quantity)
    grand_total+=item_total


    print(f"Item total : Rs{item_total:.2f}")

    print(f"Grand Total : {grand_total:.2f}")

if grand_total> 1000:
   discount =grand_total*0.1

   grand_total -= discount
   print(f"you got a discount of rs {discount:.2f}!")

  
vat = grand_total*0.13
grand_total+=vat
print(f"vat(13%):Rs {vat:.2f}")

print (f"Grand total after discoun and vat(if any): Rs{grand_total:.2f}")

