from flask import Flask
from flask import request, render_template, render_template_string


app = Flask(__name__, template_folder='')

@app.route('/')
def login_get():
    return render_template("login.html")


@app.route('/', methods=['POST',])
def login_post():
    username = request.form.get('username')
    password = request.form.get('password')
    template = '{% extends "login.html" %}{% block response %}User ' + username + ' does not exist.{% endblock %}'

    message = "User {} does not exist".format(username)
    return render_template_string(template, data=username)
    return render_template("login.html", data=username)

from datetime import datetime

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}