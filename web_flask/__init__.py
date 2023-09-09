from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def hello():
    args = {'name':'Chloe', 'contents':'November 29th 1999', 'likes':'🍦ice-cream🍦'}
    return render_template('hello.html', **args)

@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)

if __name__ =='__main__':
    app.run()