#Imports for Flask server
from flask import Flask, request, render_template
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from json import dumps

#Imports for updating the database
import time
import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from DB_Updater import job
    
scheduler = BackgroundScheduler()
scheduler.add_job(func=job, trigger="interval", hours=1)
scheduler.start()

atexit.register(lambda: scheduler.shutdown())


#Laucnhing Flask app
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///../DB/web.db'


db = SQLAlchemy(app)
class GITHUB(db.Model):
    NAME = db.Column('NAME', db.TEXT, primary_key = True)
    DESCRIPTION = db.Column(db.TEXT)
    LINK = db.Column(db.TEXT)
    FORKS = db.Column(db.INT)
    STARS = db.Column(db.INT)

def __init__(self, NAME, DESCRIPTION, LINK, FORKS, STARS):
    self.NAME = NAME
    self.DESCRIPTION = DESCRIPTION
    self.LINK = LINK
    self.FORKS = FORKS
    self.STARS = STARS

@app.route('/')
def home():
    return render_template("home.html", page = 'Acceuil')

@app.route('/developpement-logiciel')
def software():
    return render_template("software.html", repos = GITHUB.query.all(), page = 'Développement logiciel')

if __name__ == '__main__':
    app.run(debug=True)

