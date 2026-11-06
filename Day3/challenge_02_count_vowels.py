#Challenge 2 — Count vowels
sentence = input("Enter any sentence : ")
vowel_counts = 0

for letter in sentence:
    if letter.lower() in ("a","e","i","o","u"):
        vowel_counts += 1
print(vowel_counts)