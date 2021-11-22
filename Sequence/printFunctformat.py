print ("bootcamp" *  3) # the asteriks is used to multiply values
print( 2 * 5)
print("Hello\n this will print in a new line")

num1,num2=10,5
print(num1, num2, sep=',') # use of the seperator function

name = "paul"
score = 94.5
print(type(name))
print(type(score)) # the type function prints the datatype been used

# """ Format print statement"""
name = "paul"
score = 94.54567
print("hello", name, " your score is ", score) # format print statement without placeholders

# """ Use of place holders"""
print("hello %s, your score is %f"%(name, score))
print("hello %s, your score is %.2f"%(name, score)) # use of .2 to round to two decimal places

""" Use curly {} braces as placeholders """
name = "paul"
score = 94.54567
print("Your name is {1}, and your score {0}".format(score, name)) #  used as indexes


