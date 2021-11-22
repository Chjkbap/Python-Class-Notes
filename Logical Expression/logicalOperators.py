#Logical expressions evaluate to true or false.

# equal to:  == is a comparison operator. (4 == y)
# What is on the left is equal to what is on the right
num1 = 15
num2 = 20

print((num1 ==15 and num2 ==20 )) # returns true as both sides equal to true
print((num1 ==10 and num2 ==20 )) # returns false as only one side equate to true

print((num1 == 15 or num2 ==20 )) # returns true as both sides equate to true
print((num1 ==10 or num2 ==20 )) #returns true as one side equate to true

print(not(num1==15 and num2==20)) # returns  false as the "not" negates both sides
print(not(num1==10 and num2==15)) # returns true because both side equates to true

print(not(num1==15 or num2==15)) # returns false as "not" negates one side
print(not(num1==10 or num2==15)) #  returns true as "not" validates boths sides of equation




