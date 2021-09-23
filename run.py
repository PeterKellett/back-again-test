import os
from flask import Flask, render_template, url_for, flash, session

app = Flask(__name__)
app.secret_key = os.getenv("SECRET", "randomstring123")

@app.route("/")
def index():
    flash("Flash message")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
