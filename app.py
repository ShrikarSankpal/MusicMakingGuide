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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit1', methods = ['POST'])
def submit():
    if request.method == 'POST':
        scale_notes = request.form['scale_notes']
        print("User entered :\n{},{}".format(scale_notes,type(scale_notes)))
        msg = cu.getScale(scale_notes)
        #msg =[i for i in msg]
        return render_template('success.html', message="{}".format(msg))

@app.route('/submit2', methods = ['POST'])
def submit():
    if request.method == 'POST':
        chord_notes = request.form['chord_notes']
        print("User entered :\n{},{}".format(chord_notes,type(chord_notes)))
        msg = cu.getChord(chord_notes)
        return render_template('success.html', message="{}".format(msg))

if __name__ == '__main__':
    app.run()