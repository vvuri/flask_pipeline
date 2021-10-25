from flask import request, render_template, redirect, url_for

from app.dao import app, db
from app.dao.models import Message
from logger_writer import log


@app.route("/", methods=['GET'])
def hello_world():
    username = request.cookies.get('username')
    log.info(username)
    return render_template('index.html')


@app.route('/main/', methods=['GET'])
def main():
    return render_template("main.html", messages=Message.query.all())


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    db.session.add(Message(text, tag))
    db.session.commit()

    return redirect(url_for('main'))


@app.route('/about')
def about():
    return 'The about page'


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         return do_the_login()
#     else:
#         return show_the_login_form()
