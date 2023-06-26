from flask import Flask, render_template,redirect, url_for, request

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
        return redirect(url_for('guest', guest=name))
    

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' %name
    
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = str(user)))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name = str(user)))
    
@app.route('/hello/<int:score>')
def hello_name(score):
    return render_template('hello.html', marks= score)

@app.route('/result')
def result():
    dic = {'phy':50, 'chemi':60, 'maths': 70}
    return render_template('result.html', result = dic)

@app.route('/func')
def jsfunc():
    return render_template('indexpage.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/student_result', methods = ['POST', 'GET'])
def student_result():
    if request.method == 'POST':
        result = request.form
        return render_template("student_result.html", result = result)

if __name__ =='__main__':
    app.run()
