# pip install flask
# python -m pip install flask
# python -m pip install flask --user

from flask import Flask, render_template, request, redirect, url_for, session
from model import add_user, check_user, get_user_tasks
from sqlalchemy.exc import IntegrityError
from model import AccountExists, AccountNotFound

app = Flask(__name__)
app.secret_key = 'worldwidehandsomwomenQswhy'

# @app.errorhandler(404)
# def not_found(error):
#     return render_template('404.html'), 404

@app.route('/users/<name>')
def user_page(name):
    user_tasks = get_users_tasks(name)
    return render_template('user.html', name=name, tasks=user_tasks)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        try:
            name = check_user(email, password)
        except AccountNotFound:
            return render_template('index.html', error=True)
        session['account'] = name
        return redirect('/users/' + name)
    return render_template('login.html')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        password_check = request.form['password_check']
        if password_check != password:
            return render_template('index.html', error='passwords_error')
        try:
            add_user(name, email, password)
        except AccountExists:
            return render_template('index.html', error="already_exists")
        session['account'] = name
        return redirect('/users/' + name)
    return render_template('index.html')



# @app.route('/users/daniil')
# def user_daniil():
#     return 'Hello, Daniil!'

# @app.route('/users/milena')
# def user_milena():
#     return 'Hello, Milena!'

# @app.route('/users/<name>')
# def user_page(name):
#     return render_template('user.html', name=name)

@app.route('/logout')
def logout():
    # del session['username'] # рискованно
    session.pop('account', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)