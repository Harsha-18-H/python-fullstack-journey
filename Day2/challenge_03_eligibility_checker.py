#Challenge 3 — Eligibility checker
age = int(input("Enter your age : "))
graduation = input("Are you graduated : ")

if age >= 21 and graduation.upper() == "YES":
    print("Eligible")
# elif age >= 21 and graduation.upper() == "NO":
#     print("Not eligible")
# elif age < 21 and graduation.upper() == "YES":
#     print("Not eligible")
else:
    print("Not eligible")