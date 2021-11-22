varWord = "Bootcamp"
count = 0

character = input(("Enter a character: "))

for letter in varWord: # is Bootcamp
    if letter == character:
        count = count + 1
print(f"The letter{character} appears {count} times")

# practice: add an else condition if the letter is not found
