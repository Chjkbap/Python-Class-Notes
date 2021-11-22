notValidated = True

while notValidated:
    try:
        print("Enter a number: ")
        number = int(input())
        notValidated = False
    except ValueError:
        print("Enter a NUMBER")
        # number = int(input())6
        
