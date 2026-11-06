#Challenge 4 — Number comparison
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

if num1 == num2:
    print("Both the numbers are equal!")
elif num1 > num2:
    print(f"{num1} is greater than {num2}!")
else:
    print(f"{num1} is less than {num2}!")