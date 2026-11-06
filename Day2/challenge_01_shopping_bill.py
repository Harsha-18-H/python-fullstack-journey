#Challenge 1 — Shopping bill
product_price = float(input("Enter product price : "))
quantity = int(input("Enter quantity : "))

price = quantity * product_price
discount = price * (10/100)

total_price = price - discount
print(f"Total price : {total_price:.2f}")