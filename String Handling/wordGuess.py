varWord = "Bootcamp"
varUserGuess = ""
varNotguessed = varWord != varUserGuess
varGuesses = 0

while  varNotguessed and varGuesses < 5:
    if varGuesses ==1:
        varFLetter = varWord[0]
        print(f"The first letter of the word is {varFLetter}")
    elif varGuesses == 3:
        varLastLet = varWord[7]
        print(f"The last letter of the word is {varLastLet}")
    varUserGuess = input("Guess the word")
    varGuesses  = varGuesses + 1
    varNotguessed = varWord != varUserGuess

if varWord == varUserGuess:
    print("You guess correct")
else:
    print("Incorrect guess")



