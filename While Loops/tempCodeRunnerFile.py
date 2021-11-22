password = input("Enter your password: ")
passwordAttempts = 1
while password != "python" and  passwordAttempts<3:
    password = input("Please re-enter your password: ")
    passwordAttempts+=1
if password == "python":
    print("password accepted")
else:
    print("password rejected")
    # endpassRequest = input("enter")