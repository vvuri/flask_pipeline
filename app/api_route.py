from flask import Flask, request, render_template, redirect, url_for
from markupsafe import escape
from logger_writer import log
from collections import namedtuple


app = Flask(__name__)

Message = namedtuple('Message', 'text tag')
messages = []


@app.route("/", methods=['GET'])
def hello_world():
    username = request.cookies.get('username')
    log.info(username)
    return render_template('index.html')


@app.route('/main/', methods=['GET'])
def main():
    return render_template("main.html", messages=messages)


@app.route('/add_message', methods=['POST'])
def add_message():
    text = request.form['text']
    tag = request.form['tag']

    messages.append(Message(text, tag))

    return redirect(url_for('main'))


# @app.route('/post/<int:post_id>')
# def show_post(post_id):
#     # show the post with the given id, the id is an integer
#     return f'Post {post_id}'
#
#
# @app.route('/path/<path:subpath>')
# def show_subpath(subpath):
#     # show the subpath after /path/
#     return f'Subpath {escape(subpath)}'


@app.route('/about')
def about():
    return 'The about page'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()
