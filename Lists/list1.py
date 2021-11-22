list1 = []
print(list1)
list1.append("Python")
print(list1)

list1.insert(1,"HTML")
print(list1)

lst2 = []
lst2.insert(0,"SQL")
lst2.append("CSS")
print(lst2)

lst3 = [10, 20, "JavaScript", 10.5]
print(lst3)

print(lst3[1:3])

del(lst3[3])
print(lst3)
lst4 = [10, 20,-1, 10.5, 6]
print(max(lst4))
print(min(lst4))

lst4.sort()
print(lst4)

lst4.sort(reverse=True)
print(lst4)



lst4.clear()
print(lst4)

lst3.remove("JavaScript")
print(lst3)