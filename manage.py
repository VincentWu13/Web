import os

import flask
from flask import render_template, send_file

app = flask.Flask('Vincent', template_folder='html')
port = os.environ.get('PORT')
print(port)


@app.route('/')
def homepage():
    return render_template(
        'index.html')


@app.route('/index.html')
def homepage_2():
    return render_template(
        'index.html')


@app.route('/diary_1.html')
def diary_1():
    return render_template(
        'diary_1.html')


@app.route('/diary_2.html')
def diary_2():
    return render_template(
        'diary_2.html')


@app.route('/<path:path>')
def return_file(path):
    return send_file(path)


if __name__ == "__main__":
    app.run(port=port)
