import cgi, cgitb, mysql.connector
form = cgi.FieldStorage()
#if form.getvalue('q1'):

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	passwd="Chimichangas",
	database="enterdata"
)

mycursor=mydb.cursor()

q1 = form.getvalue('q1')
q2 = form.getvalue('q2')
q3 = form.getvalue('q3')
q4 = form.getvalue('q4')

#cmd="INSERT INTO Answers (Qno, Ans) VALUES (%s, %s)"
#cmd="REPLACE INTO Answers (Qno, Ans) VALUES (%s, %s)"
cmd="DELETE * FROM Answers"
val = [
	('1', q1), 
	('2', q2), 
	('3', q3), 
	('4', q4), 
]

mycursor.execute("DELETE * FROM Answers")#, val)
mydb.commit()