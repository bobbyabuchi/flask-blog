import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import python datetime object
from datetime import date, datetime

app = Flask(__name__)

# App config DB location - the DB URI, so SQLAlchemy will create the DB and store it in this location
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/mark/repo200/flask-blog/flask-blog.db'
db = SQLAlchemy(app)

# after specifying your DB URI, create your database
# terminal -> project directory 
# >>> sqlite3 databasename.db
# >>> .tables # call tables

# check if data was inserted successfully
# >>> sqlite3 flask-blog # select DB
# >>> .tables # show tables
# >>> select * from tablename;

# >>> .exit # exit the sqlite3


# create table for the blog posts
class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    subtitle = db.Column(db.String(60))
    author = db.Column(db.String(60)) 
    date = db.Column(db.DateTime)
    content = db.Column(db.Text)

# So when you're done with the block of code above, get into the terminal and do...to create the table and columns we already specified
# >>> python3
# >>> from app import db
# >>> db.create_all()


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/education')
def education():
    return render_template('education.html')

# enable users to add blog post to the database
@app.route('/add')
def add():
    return render_template('add.html')

# for the submit button
@app.route('/addpost', methods=['POST'])
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']
    # used this return for testing
    # return '<h1>Title: {} Subtitle: {} Author: {} Content: {}</h1>'.format(title, subtitle, author, content, date=datetime.now())

    post = Blogpost(title=title, subtitle=subtitle, author=author, content=content, date=datetime.now())

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)