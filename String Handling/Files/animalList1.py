# Replacing items in 1D list
words = ["Dog", "Fish", "Cat"]
print(words)
words[0] = "Cow"
print(words)

# appent to 1D list
words = ["Dog", "Fish", "Cat"]
words.append("Cow")


# Replacing items in 2D list
animals = [["Salmon", "Pollock", "Cod"],
           ["Parrot", "Duck", "Wren"],
           ["Camel", "Lion", "Tiger"]]
        
# Replace item in row 0 at index location 2 with Plaice
animals[0][2] = "Plaice" 

#append to 2D lis
#2D list, then it will just 
# add another element to the end list structure.
animals = [["Salmon", "Pollock", "Cod"],
           ["Parrot", "Duck", "Wren"],
           ["Camel", "Lion", "Tiger"]]      
animals.append("Trout")
print(animals)

#to append a specific list within the 
#2D list, then you specify which list. 
animals[0].append("Trout")
print(animals)


