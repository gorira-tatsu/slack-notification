from flask import Flask
from flask import redirect
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def button():
    if request.method == 'POST':
        if request.form['send'] == 'push':
            import slack
            return render_template('index.html')
    elif request.method == 'GET':
          return render_template('index.html')