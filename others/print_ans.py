import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Chimichangas",
	database="enterdata"
)

mycursor=mydb.cursor()

mycursor.execute("SELECT * FROM Answers")
myresult=mycursor.fetchall()

for x in myresult:
	print(x)