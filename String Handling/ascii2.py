# chr(): Takes a decimal returns the ascii equivalent character 
# ord(): Takes a charcter and returns the decimal equivalent  

varMsg = ""
varLetter = input("Enter a single letter: ")
varConvert = ord(varLetter)
varMsg = varMsg + str(varConvert)
print(varMsg)


#Array features
# fixed in size, contain data of the same type, 
# contents can be changed but cannot be added or deleted 
arrayNumbers = [1,2,3,4,5] 