cursor.execute("select * from members") #invoke the cursor method to store data

#fetch/retrieve one record at a time 

row = cursor.fetchone()
while row is not None: #loop through each row
    print(row) # return the results
    row=cursor.fetchone() 
cursor.close
conn.close