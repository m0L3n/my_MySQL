#!/usr/bin/python
import MySQLdb

### INSERT Operation ###

# DB connection
db = MySQLdb.connect("")
#cursor object
cursor = db.cursor()
# query to inserc record to db
sql = """ INSERT INTO STUDENT(NAME,SURENAME, ROLL_NO)
            VALUES('Torsten','Mueller',1)"""
try:
    #exec query
    cursor.execute(sql)
    #commit to db
    db.commit()
except:
    #in case of any accuring error
    db.rollback()

# disconnect from server
db.close

#READ Operation

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT * FROM STUDENT"
try:
     # execute sql
     cursor.execute(sql)
     # Fetch all the rows in a list of lists.
     results = cursor.fetchall()
     for row in results:
         f_name = row[0]
         l_name = row[1]
         id = row[2]
     # print fetched result
     #Print("name=%s,surname=%s,id=%d" % \ (f_name, l_name, id ))
except:
 print("Error: unable to fetch the data")
