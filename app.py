# these first 2 lines are only for on the school system
import sys

sys.path.append('N:\python-modules')

from flask import Flask, render_template, request, redirect
import sqlite3
from sqlite3 import Error
from datetime import datetime

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
    # drop_blog_table = """DROP TABLE entry"""
    # create_table(con, drop_blog_table)
    create_blog_table = """CREATE TABLE IF NOT EXISTS entry(
                            id integer PRIMARY KEY,
                            title text NOT NULL,
                            body text NOT NULL,
                            posttime datetime NOT NULL
                            )"""
    create_table(con, create_blog_table)


@app.route('/')
def hello_world():
    con = create_connection(DATABASE_NAME)
    get_entries = """SELECT id, title, body, date(posttime) AS date, time(posttime) AS time FROM entry ORDER BY posttime DESC;"""
    cur = con.cursor()

    cur.execute(get_entries)
    entries = cur.fetchall()
    for entry in entries:
        print(entry)

    return render_template("home.html", entries=entries)


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
    now = datetime.now()
    post = (title, body, now)
    sql = """INSERT INTO entry(title, body, posttime) VALUES (?,?,?);"""
    cur = con.cursor()
    cur.execute(sql, post)
    con.commit()
    con.close()

    return redirect('/')


@app.route('/do-delete-post/<post_id>')
def do_delete_post(post_id):
    con = create_connection(DATABASE_NAME)
    sql = """DELETE FROM entry WHERE id=?"""
    cur = con.cursor()
    cur.execute(sql, (post_id,))
    con.commit()
    con.close()

    return redirect('/')


if __name__ == "__main__":
    app.run()
