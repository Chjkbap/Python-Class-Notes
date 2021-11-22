# holds more than one list, know two dimensional/multi dimensional

# row 0 holds the names
#row 1 holds the scores
scoreList = [ 
[ "Tom", "Yulia", "Hassan","Askhan", "Kavitha", "David"],  
[1, 2, 3,4, 5, 6],
[ "Pyhon", "HTML", "CSS","JavaScript", "SQL", "NoSQL"]
]

scoreList[2][5] ="Java"
print(scoreList)

scoreList[0].append("Lucy")
print(scoreList)

print(scoreList)
# acessing 2d list
print(scoreList[0][3])
print(scoreList[0][1])
print(scoreList[0][2])
print(scoreList[0][1:3])

#Exercise 5. Create a 2D list with 6 items 
# name of your choice 
# print the 2nd, 4th and last item in he list
print(scoreList[2][3])
