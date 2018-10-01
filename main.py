from flask import Flask, render_template
import os
import jinja2
import cgi
from flask import request

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader (template_dir))


app = Flask(__name__)
app.config['DEBUG'] = True



@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route("/check", methods = ['Post'])
def check():
    username = request.form['username']
    password = request.form['password']
    vpassword = request.form['vpassword']
    email = request.form['optional']

    usernameCheck =""
    passwordCheck=""
    vpasswordCheck=""
    emailCheck=""

    vd = "Enter a valid email address."

    if username =="":
        usernameCheck = "Please enter a username."

    if password =="":
        passwordCheck ="Please enter a password"
    if len(password)<=3:
        passwordCheck = "Password is too short."
    if len(password)>=20:
        passwordCheck = "Password is too long."
    if (" " in password):
        passwordCheck = "Password cannot contain a space."

    if password!=vpassword:
        passwordCheck = "Passwords do not match."

    if email !="":
        if (" " in email):
            emailCheck = vd
        if len(email)<=3:
            emailCheck = vd
        if len(email)>=20:
            emailCheck = vd
        if email.count('@')!=1:
            emailCheck=vd
        if email.count('.')!=1:
            emailCheck=vd
        
    if usernameCheck=="" and passwordCheck=="" and vpasswordCheck=="" and emailCheck=="":
        template = jinja_env.get_template('welcome.html')
        return template.render()

    template = jinja_env.get_template('check.html')
    return template.render(username=username, usernameCheck = usernameCheck, password = password,passwordCheck=passwordCheck,vpassword=vpassword,vpasswordCheck=vpasswordCheck, email=email, emailCheck=emailCheck) 


app.run()