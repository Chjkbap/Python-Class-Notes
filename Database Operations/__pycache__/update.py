from pythonCon import *

upd = "UPDATE songs SET artist = 'Python' WHERE SongID = 5"
cursor.execute(upd)  
print("Record Updated")