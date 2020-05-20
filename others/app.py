from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class answers(db.Model):
    id = db.Column('ans_id', db.Integer, primary_key=True)
    a1 = db.Column(db.String(5))
    a2 = db.Column(db.String(5))
    a3 = db.Column(db.String(5))
    a4 = db.Column(db.String(5))
    #id = db.Column(db.Integer, primary_key=True)
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    # def __repr__(self):
        # return '<Dataclass %r>' % self.data
    #def __str__(self):
     #   return "{} {} {} {}".format(self.q1, self.q2, self.q3, self.q4)

@app.route('/')
def index():
    return render_template('introduction.html')

@app.route("/add", methods=['GET', 'POST'])
def table_add():
    if request.method == 'POST':
        if not request.form['q1'] or not request.form['q2'] or not request.form['q3'] or not request.form['q4']:
            flash('Please answer all the MCQs. They are compulsory.', 'error')
        else:
            answer=answers(request.form['q1'], request.form['q2'], request.form['q3'], request.form['q4'])
        db.session.add(answer)
        db.session.commit()
        flash('Answers submitted')
        return redirect(url_for('show_all'))
        # db.create_all()
        # new_data=Answers(data)
        #db.session.add(data)
        # db.session.commit()
    # temp ={}
    # temp['status']=(type(new_data)==Answers)
    # return jsonify(temp)
    #flash('Answers submitted')
    return render_template('new.html')

@app.route('/introduction')
def introduction():
    return render_template('introduction.html')


@app.route('/theory')
def theory():
    return render_template('theory.html')


@app.route('/objective')
def objective():
    return render_template('objective.html')


@app.route('/experiment')
def experiment():
    # db.create_all()
    # allDataclasss=Dataclass.query.all()
    # strf = ''
    # for d in allDataclasss:
    #     strf += d.data
    return render_template('experiment.html')


@app.route('/quizes')
def quizes():
    # db.create_all()
    return render_template('quizes.html')


@app.route('/procedure')
def procedure():
    return render_template('procedure.html')


@app.route('/further_reading')
def furtherReading():
    return render_template('further_reading.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
