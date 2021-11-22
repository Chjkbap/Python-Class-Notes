from random import randint

for i in range(3):
  num1 = randint(2, 10)
  num2 = randint(2, 10)
  numSum = num1 * num2
  
  randNums = int(input(f"{num1} * {num2} = "))
  
  if randNums == numSum:
    print("Well done you got it right!")
  else:
    print("Sorry wrong answer")

#what names would you use for a, b, c, d 