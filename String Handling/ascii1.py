# chr(): Takes a decimal returns the ascii equivalent character 
# ord(): Takes a charcter and returns the decimal equivalent  

varMsg = ""
varNum = int(input("Enter a number"))
varConvert = chr(varNum)
varMsg = varMsg + varConvert
print(varMsg)
