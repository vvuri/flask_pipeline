from flask import request, render_template, redirect, url_for, flash, jsonify
from flask_login import login_user, login_required, logout_user
from werkzeug.security import check_password_hash, generate_password_hash

from app.dao import app, db
from app.dao.models import Message, User
from logger_writer import log


@app.route('/', methods=['GET'])
def root_page(self):
    username = request.cookies.get('username')
    log.info(username)
    return render_template('index.html')


@app.route('/main/', methods=['GET'])
@login_required   # необходима авторизация на странице
def main():
    return render_template("main.html", messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
@login_required
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    db.session.add(Message(text, tag))
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    login = request.form.get("login")
    password = request.form.get("password")

    if login and password:
        user = User.query.filter_by(login=login).first()
        if check_password_hash(user.password, password):
            login_user(user)
            # что бы избежать сразу переход пользователя на нужную страницу без авторизации
            next_page = request.args.get('next')
            redirect(next_page)
        else:
            # сообщения которые можем использовать где-либо
            flash('Incorrect login or password')
    else:
        flash('Please fill login and password')
        return render_template("login.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    login = request.form.get("login")
    password = request.form.get("password")
    password2 = request.form.get("password2")

    if request.method == 'POST':
        if not (login and password and password2):
            flash('Please, fill all fields')
        elif password != password2:
            flash('Password are not equal')
        else:
            hash_pass = generate_password_hash(password)
            new_user = User(login=login, password=hash_pass)
            db.session.add(new_user)
            db.session.commit()

            return render_template('login.html')
    else:
        return render_template("register.html")


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return render_template("index.html")


@app.after_request
def redirect_to_sign_in(response):
    if response.status_code == 401:
        return redirect(url_for("login_page") + '?next=' + request.url)

    return response
