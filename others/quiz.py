import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Chimichangas"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")