import time
startTimeSecs = time.time()
print(startTimeSecs)
formattedStarTime = time.ctime(startTimeSecs)

hrs = int(input("Input hours of parking required ( 2, 4, or 12)"))
numInSecs = hrs * 60 * 60
if hrs == 2:
    charge = 3.00
elif hrs == 4:
    charge = 4.10
else:
    charge =9.00
endTimeInSecs =startTimeSecs + numInSecs
print("\nTime now :", formattedStarTime )
endFormattedTimed = time.ctime(endTimeInSecs)
print("Expires: ", endFormattedTimed)
print(f"Charge = {charge}")

