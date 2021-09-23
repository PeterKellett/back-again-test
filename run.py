import os
from flask import Flask, render_template, url_for, flash, session, request, redirect

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', '')

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
            return redirect(url_for('index'))
        else:
            flash("username and/or password is incorrect, please try again.", "error")
            return render_template('login.html')
    else:
        return render_template('login.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
