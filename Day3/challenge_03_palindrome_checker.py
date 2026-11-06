#Challenge 3 — Palindrome checker
word = input("Enter any word : ")

if word.lower() == word[::-1]:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")