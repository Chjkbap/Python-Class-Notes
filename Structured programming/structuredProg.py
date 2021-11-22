guess = 3
notGuessed = True
while notGuessed:
    number = int(input("Guess a number: "))
    if number == guess:
        break
    print(f" You gessed {number} ")