from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    args = {'title':'index page', 'contents': 'hello world'}
    return render_template('index.html', **args)
