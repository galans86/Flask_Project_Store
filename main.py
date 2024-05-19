from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/index/")
def index():
    context = {
        'name': 'G A L I N A',
    }
    return render_template('index.html', **context)

@app.route("/clothes/")
def clothes():
    return render_template('clothes.html')

@app.route("/boots/")
def boots():
    return render_template('boots.html')

@app.route("/coats/")
def coats():
    return render_template('coats.html')
