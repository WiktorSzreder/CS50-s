str = input("Input: ")

for letter in str:
    if letter.lower() not in "aeiou":
        print(letter, end="")