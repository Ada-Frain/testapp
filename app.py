# pip install flask
# python -m pip install flask
# python -m pip install flask --user

from flask import Flask, render_template, request, redirect, url_for
from modul import add_user

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # return 'Test'
    # return {'data': ['apple', 'pie']}
    # return '<h1>Test</h1>'
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_check = request.form['password_check']
        add_user(name, email, password)
        # print(request.form['name'])
        return redirect('/users/' + name)
    return render_template('index.html')



# @app.route('/users/daniil')
# def user_daniil():
#     return 'Hello, Daniil!'

# @app.route('/users/milena')
# def user_milena():
#     return 'Hello, Milena!'

@app.route('/users/<name>')
def user_milena(name):
    return render_template('user.html', name=name)

app.run(debug=True)