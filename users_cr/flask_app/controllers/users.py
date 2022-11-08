from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    return render_template('index.html', all_users = users)

@app.route('/adduser')
def addUser():
    return render_template('adduser.html')

@app.route('/submit', methods=["POST"])
def submitUser():
    if not User.validate_users():
        return redirect('/adduser')
    User.save(request.form)
    return redirect('/')

