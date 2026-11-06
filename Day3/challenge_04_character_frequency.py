#Challenge 4 — Character frequency
#method 1:
# word = "programming"
# character = "g"

# print(word.count(character))

#method 2:
word = "programming"
character = "g"
count = 0

for char in word:
    if char == character:
        count += 1
print(count)
    