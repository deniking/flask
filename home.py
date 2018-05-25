from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def hello_word(name):
    return 'Hello World!'

@app.route("/user/<sopo>")
def user(sopo):
    return 'Hai Users %s!' % sopo

@app.route('/main/<type>')
def main(type):
    return 'Main %s' % type
