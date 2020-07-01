from application import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World"


@app.route('/login')
def login():
    return render_template('login-page.html')
