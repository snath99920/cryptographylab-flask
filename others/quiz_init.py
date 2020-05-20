from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'

db = SQLAlchemy(app)

class Answers(db.Model):
#	qno = db.Column(db.Integer)
	Ans = db.Column(db.String(10))

def __init__(self, qno, Ans):
	self.Ans = Ans