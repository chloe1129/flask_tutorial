from flask import Flask, render_template

app = Flask(__name__)

# variable: <variable-name>
@app.route("/hello/<name>")
def hello(name):
    args = {'title':'This is index page', 'contents': 'hello %s !' % name}
    return render_template('index.html', **args)
    # return 'Hello %s :)' % name

if __name__ =='__main__':
    app.run()
