#Challenge 5 — Simple bill calculator
product_name = input("Enter product name : ")
quantity = int(input("Enter purchased quantity : "))
price_per_item = 33

total_bill = price_per_item * quantity

print(f"Total bill :\n{product_name}        {quantity} * {price_per_item}      :       {total_bill}")
