pyCourse = float(input("Enter your python score"))
htmlCourse = float(input("Enter your HTML score"))
sqlCourse = float(input("Enter your SQL score"))

if pyCourse < 45:
    print(f"Try again in python {pyCourse}")
elif htmlCourse < 45:
    print(f"Try again in HTML {htmlCourse}")
elif sqlCourse < 45:
    print(f"Try again in SQL {sqlCourse}")

else:
    gradesAverage = (pyCourse + htmlCourse + sqlCourse)/ 3
    if gradesAverage <= 55:
         print(f" Your score is {gradesAverage} and is Grade C ")
    if gradesAverage <= 79:
         print(f" Your score is {gradesAverage} and is Grade B")
    if gradesAverage <= 89:
         print(f" Your score is {gradesAverage} and is Grade B ")


