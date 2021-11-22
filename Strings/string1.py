# emptyString = ""

s1 =   "     This is a Bootcamp   "
sPos = "01234567"
s2 = "Python"
print(f"This is {s2} {s1} ")

print(s1[1], s1[2], s1[3], s1[4]) # print characters as per index position

print("There are", len(s2), "characters in", s2)# use len to chech number of characters

""" Slicing list"""

print(s2[3:5])
print(s2[2:])
print(s2[:4])

"""Slicing/printing using negative index"""
print(s2[-4:-1])

""" steps in slicing"""

print(s1[0:9:2])

"""print in reverse order"""
print(s2[7::-1])
print(s1[::-1])
"""Strip spaces using strip function"""
print(s1.strip())
print(s1) # without strip
print(s1.lstrip())
print(s1.rstrip())


"""Find/locate word in a sentence"""
s3 = "It is a beautiful day"

print(s3.find("day"))
print(s3.find("beautiful",0,len(s3)))
print(s3.count("a"))
print(s3.replace("day", "weather"))
print(s2.upper())
print(s2.lower())
s4 = "ms"
print(s4.title())