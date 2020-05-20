import os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, jsonify
from flask_sqlalchemy import SQLAlchemy
from dss import DSS
import json

dsO = DSS()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'    #Declare and connect to database
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)

class answers(db.Model):
    '''a1, a2, a3, a4, a5, a6, a7 become columns of the table that we are making, i.e. answers'''
    id = db.Column('ans_id', db.Integer, primary_key=True)
    a1 = db.Column(db.String(5))
    a2 = db.Column(db.String(5))
    a3 = db.Column(db.String(5))
    a4 = db.Column(db.String(5))
    a5 = db.Column(db.String(200))
    a6 = db.Column(db.String(200))
    a7 = db.Column(db.String(200))

    def __init__(self, a1, a2, a3, a4, a5, a6, a7):
        self.a1 = a1;
        self.a2 = a2;
        self.a3 = a3;
        self.a4 = a4;
        self.a5 = a5;
        self.a6 = a6;
        self.a7 = a7;
    
@app.route('/')     #Home page gives introduction
def index():
    return render_template('introduction.html')

@app.route('/api/hash')
def hash():
    val = str(request.args.get('val'))
    dsO.set_message(val)
    h = dsO.gen_hash()
    res = {'hash': h}
    return json.dumps(res)

@app.route('/api/generate')
def generate_keys():
    e = int(request.args.get('e'))
    bits = int(request.args.get('sz'))
    if e==0:
        e = 65537
    key = dsO.gen_keys(2*bits, e)
    res = {'e': e, 'key': key}
    return json.dumps(res)

@app.route('/api/encrypt')
def encrypt():
    h = str(request.args.get('h'))
    ds, ds64 = dsO.gen_DS(h)
    res = {'ds': ds, 'ds64': ds64}
    return json.dumps(res)

@app.route('/show', methods=['GET', 'POST'])
def show_all():
    return render_template('show_all.html', answers = answers.query.all())

@app.route('/quizes', methods=['GET', 'POST'])
# os.remove('students.sqlite3')
def quizes():
    os.remove('students.sqlite3')   #Remove database after use so that it can be recreated and the values can be refreshed
    db.create_all()
    '''The following lines helps handle the error when no or some answers in the quiz are selected'''
    if request.method == 'POST':
        try:
            a1 = request.form['a1']
        except:
            a1=""

        try:
            a2 = request.form['a2']
        except:
            a2=""

        try:
            a3 = request.form['a3']
        except:
            a3=""

        try:
            a4 = request.form['a4']
        except:
            a4=""
        
        answer = answers(a1, a2, a3, a4, request.form['a5'], request.form['a6'], request.form['a7'])
        db.session.add(answer)
        db.session.commit()
        flash('Answers submitted')
        return redirect(url_for('show_all'))
    return render_template('quizes.html')

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
    return render_template('experiment.html')

@app.route('/procedure')
def procedure():
    return render_template('procedure.html')

@app.route('/further_reading')
def furtherReading():
    return render_template('further_reading.html')

if __name__ == '__main__':
    db.create_all()
    # os.remove('students.sqlite3')
    app.run(debug=True)