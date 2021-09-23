import os
from flask import Flask, render_template, url_for, flash, session, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONJS'] = False

db = SQLAlchemy(app)

class = users(bd.model):
    _id = db.column("id", db.Integer, primary_key=True)
    name = db.column("id", db.String(100))
    email = db.column("id", db.String(100))

    def __init__(self, name, email):
        self.name = name
        self.email = email


@app.route("/")
def index():
    if 'username' in session:
        flash('Registered Success!!', 'success')
    else:
        flash('You are not logged in', 'warning')
    return render_template("index.html")


@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == 'POST':
        attempted_username = request.form['username']
        attempted_password = request.form['password']

        #flash(attempted_username)
        #flash(attempted_password)

        if attempted_username == "admin" and attempted_password == "password":
            session['username'] = request.form['username']
            return redirect(url_for('about'))
        else:
            flash("username and/or password is incorrect, please try again.", "error")
            return redirect(url_for('login'))
    else:
        return render_template('login.html')


@app.route('/about', methods=["POST", "GET"])
def about():
    email = None
    if 'username' in session:
        flash('Welcome back.', 'success')
        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("Your email was saved.")
        else:
            if "email" in session:
                email = session["email"]
        return render_template('about.html', email=email)
    else:
        flash('Access denied!', 'error')
        return redirect(url_for('login'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
