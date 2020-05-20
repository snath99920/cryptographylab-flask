import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Chimichangas",
	database="mydatabase"
)

mycursor=mydb.cursor()
mycursor.execute("CREATE TABLE Answers (Qno VARCHAR(255), Ans VARCHAR(255))")

cmd="INSERT INTO Answers (Qno, Ans) VALUES (%s, %s)"
val = [
	('1', 'b'), 
	('2', 'a'), 
	('3', 'b'), 
	('4', 'b'), 
]

mycursor.executemany(cmd, val)
mydb.commit()
