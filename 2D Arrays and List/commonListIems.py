aList = ["Tom", "Yulia", "Hassan","Askhan", 
"Kavitha", "David","Ben"]

bList =["Ben", "Askhan", "Kavitha",
 "David", "Chetana", "Jay", "Sajid"]

cList =[]

cList =[ names for names in aList if names in bList ]
print(cList)