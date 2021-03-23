from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

import collectionUtils as cu

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#class scalesData(db.nodel):
#    __tablename__='scalesData'
#    note = db.Column(db.String(2))



@app.route('/')
def index():
    return render_template('index.html', message=cu.sendDict())

@app.route('/submit1', methods = ['POST'])
def submit1():
    if request.method == 'POST':
        scale_notes = request.form['scale_notes']
        print("User entered :\n{},{}".format(scale_notes,type(scale_notes)))
        msg = cu.getScale(scale_notes)
        #msg =[i for i in msg]
        return render_template('success.html', message=msg)

@app.route('/submit2', methods = ['POST'])
def submit2():
    if request.method == 'POST':
        chord_notes = request.form['chord_notes']
        print("User entered :\n{},{}".format(chord_notes,type(chord_notes)))
        msg = cu.getChord(chord_notes)
        return render_template('success.html', message=msg)

@app.route('/submit3', methods = ['POST'])
def submit3():
    if request.method == 'POST':
        scale_base_note = request.form['scale_base_note']
        scale_type = request.form['scale_type']
        print("User entered :\n{},{},{},{}".format(scale_base_note,type(scale_base_note), scale_type, type(scale_type)))
        msg = cu.getScaleNotes(scale_base_note, scale_type)
        return render_template('success.html', message=msg)

@app.route('/submit4', methods = ['POST'])
def submit4():
    if request.method == 'POST':
        chord_base_note = request.form['chord_base_note']
        chord_type = request.form['chord_type']
        print("User entered :\n{},{},{},{}".format(chord_base_note,type(chord_base_note), chord_type, type(chord_type)))
        msg = cu.getChordNotes(chord_base_note, chord_type)
        return render_template('success.html', message=msg)

if __name__ == '__main__':
    app.run(host='127.0.0.1')