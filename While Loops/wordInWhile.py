print("Guess the word")
guessWord = input("Enter your guess word: ")
while  guessWord != "bootcamp":
    print("Try again")
    guessWord = input()
print(f"Well done you have guess the word, {guessWord}")
