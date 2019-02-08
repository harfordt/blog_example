# these first 2 lines are only for on the school system
import sys

sys.path.append('N:\python-modules')

from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("home.html")


@app.route('/profile')
def profile():
    return render_template("profile.html")


@app.route('/gallery')
def gallery_page():
    return render_template("gallery.html")


if __name__ == "__main__":
    app.run()
