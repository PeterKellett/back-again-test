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
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
