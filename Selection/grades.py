mark = int(input("Enter a mark: "))

if mark >=75:
    grade ="A"
elif mark >= 60:
    grade = "B"
elif mark >= 50:
    grade = "C"
else:
    grade = "F"
print(f"Your grade is {grade}")