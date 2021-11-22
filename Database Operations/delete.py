from pythonCon import *

def delete(MemberID):
    try:
        strDel = "DELETE FROM members where MemberID='%d'"
        args=(MemberID)
        cursor.execute(strDel % args )  
        print("Record deleted")
        conn.commit()
    except:
        conn.rollback()
    
    finally:
        cursor.close
        conn.close()
memID = int(input("Enter Member ID: ")) # create memID variable to store the member id to be deleted
delete(memID) # 


