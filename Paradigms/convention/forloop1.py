"""What is wrong with this program?
Describe the convention that has been broken here. 
"""
import time
from random import randint
count = 10

time_taken = 0 

numbers = []




for second in range(count):
    numbers.append(randint(0, 100))
    time.sleep(1)
    time_taken += 1

print(numbers)
print(time_taken)

