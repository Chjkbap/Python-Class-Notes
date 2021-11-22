from pythonCon import *

try:
    cursor.execute("INSERT INTO songs ( `Title`, `Artist`, `Genre`) VALUES ( 'VScode Python issues', 'Microsoft', 'Not for Python')")
    print("record inserted")

    conn.commit()
except: 
    conn.rollback()
cursor.close
conn.close()
