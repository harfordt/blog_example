# these first 2 lines are only for on the school system
import sys

sys.path.append('N:\python-modules')

from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error


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

@app.route('/new-blog-post')
def new_blog_post():
    return render_template("new_blog_post.html")





@app.route('/do-insert-blog-post', methods=['POST'])
def do_insert_blog_post():
    title = request.form['title']
    body = request.form['body']
    print(title)
    print(body)

    return redirect('/')




if __name__ == "__main__":
    app.run()
