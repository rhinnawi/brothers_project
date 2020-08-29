#!usr/bin/env python

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/rani')
def rani():
    return render_template('rani.html')

@app.route('/tammir')
def tammir():
    return render_template('tammir.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)