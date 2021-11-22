from pythonCon import *

upd = "UPDATE songs SET artist = 'Python' WHERE SongID = 5"
cursor.execute(upd)  
print("Record Updated")







# def update():#SongID, genre):
#     try:
#         # strUpd = "UPDATE songs SET genre= %s where SongID = %d"
#         # args=(SongID, genre)
#         # cursor.execute(strUpd % args )  
#         # print("Record Updated")
#         # conn.commit()
#         upd = "UPDATE songs SET genre = 'Culture' WHERE SongID = 2;"
#         cursor.execute(upd)  
#         print("Record Updated")
#         conn.commit()
#     except:
#         conn.rollback()
    
#     finally:
#         cursor.close
#         conn.close()
# # memID = int(input("Enter Member ID ")) # create memID variable to store the member id to be deleted
# # email = (input("Enter email: "))
# # Email = ""
# # update(MemberID =memID , Email= email)
# # update(1, 'Culture ***')
# # print(test)
# update()



upd = "UPDATE songs SET artist = 'Python' WHERE SongID = 5"
cursor.execute(upd)  
print("Record Updated")
conn.commit()



# def update():#SongID, genre):
#     try:
        # upd = "UPDATE songs SET genre = '%s' WHERE SongID = '%s'"
        # # intVal = (int(input("Enter Song ID ")))
        # # strVal = (input("Enter Genre "))
        # intVal = 1
        # strVal = "testets"
        # cursor.execute(upd, intVal, strVal)  
        # conn.commit()
        # print("Record Updated")
    # except:
    #     conn.rollback()
    
    # finally:
    #     cursor.close
    #     conn.close()
# update()

# upd = "UPDATE songs SET genre = %s WHERE SongID = %d"
        # intVal = (int(input("Enter Song ID ")))
        # strVal = (input("Enter Genre "))
# intVal =1
# strVal = 'testets'
# cursor.execute(upd, intVal, strVal)  
# conn.commit()
# print("Record Updated")
