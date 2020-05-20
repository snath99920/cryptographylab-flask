import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Chimichangas"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE enterdata")
mycursor.execute("CREATE TABLE Answers (Qno VARCHAR(255), Ans VARCHAR(255))")

cmd="INSERT INTO Answers (Qno, Ans) VALUES (%s, %s)"

val = [
	('1', 'a'), 
	('2', 'a'), 
	('3', 'a'), 
	('4', 'a'), 
]

mycursor.executemany(cmd, val)
mydb.commit()