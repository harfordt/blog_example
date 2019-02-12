# these first 2 lines are only for on the school system
import sys

sys.path.append('N:\python-modules')

from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error

DATABASE_NAME = "blog.db"
app = Flask(__name__)


def create_connection(db_file):
    """create a connection to the sqlite db"""
    try:
        connection = sqlite3.connect(db_file)
        initialise_tables(connection)
        return connection
    except Error as e:
        print(e)

    return None


def create_table(con, query):
    if con is not None:
        try:
            c = con.cursor()
            c.execute(query)
        except Error as e:
            print(e)


def initialise_tables(con):
    create_blog_table = """CREATE TABLE IF NOT EXISTS entry(
                            id integer PRIMARY KEY,
                            title text NOT NULL,
                            body text NOT NULL
                            )"""
    create_table(con, create_blog_table)


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
    return render_template("new-blog-post.html")


@app.route('/do-insert-blog-post', methods=['POST'])
def do_insert_blog_post():
    title = request.form['title']
    body = request.form['body']
    print(title)
    print(body)

    con = create_connection(DATABASE_NAME)
    post = (title, body)
    sql = """INSERT INTO entry(title, body) VALUES (?,?);"""
    cur = con.cursor()
    cur.execute(sql, post)
    con.commit()
    con.close()

    return redirect('/')


if __name__ == "__main__":
    app.run()
