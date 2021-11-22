from pythonCon import *

try:
    def delete(MemberID):
        vDel = "DELETE FROM members where MemberID='%d'"
        args = (MemberID)
        cursor.execute(vDel % args )
        print("record deleted")
        conn.commit()
except:
    conn.rollback()

finally:
    cursor.close
    conn.close()
memID = int(input("Enter memberId you want to delete: "))
delete(memID)