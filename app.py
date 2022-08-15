from flask import Flask
app = Flask(__name__)
@app.route('/')

@app.route('/')
def hello_world():
    return 'Hello world'

export FLASK_APP=app.py

flask run

