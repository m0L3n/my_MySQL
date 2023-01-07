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