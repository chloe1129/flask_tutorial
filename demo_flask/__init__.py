from flask import Flask, render_template,redirect, url_for

app = Flask(__name__)

# variable: <variable-name>
@app.route("/hello")
def index():
    args = {'name':'chloe'}
    return render_template('index.html', **args)

@app.route("/perfect/<chloe>")
def hello_chloe(chloe):
    args = {'contents': 'hello my name is %s !' % chloe}
    return render_template('chloe.html', **args)


@app.route('/guest/<guest>')
def guest(guest):
    args = {'guest': 'hello my name is %s !' % guest}
    return render_template('guest.html', **args)

# variable: <variable-name>
@app.route("/hello/<name>")
def hello_user(name):
    if name == 'chloe':    
        return redirect(url_for('hello_chloe', chloe=name))
    else:
        return redirect(url_for('guset', guset=name))

if __name__ =='__main__':
    app.run()
