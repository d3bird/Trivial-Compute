from flask import Flask 
from flask import render_template
from flask import request
from flask import url_for
from flask import flash
from flask import redirect
from werkzeug.exceptions import abort

import SQL.commonSQLfunctions
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'exampleSecretKey'

@app.route('/')
def index():
    #this should be the lobby page
    return render_template('index.html')

#@app.route('/about')
#def about():
#    return render_template('about.html')

def getQuestion(post_id):
    conn = sqlite3.connect("SQL/questionDatabase.db")
    conn.row_factory = sqlite3.Row
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/question/<int:post_id>')
def post(post_id):
    post = getQuestion(post_id)
    return render_template('single_question.html', post=post)

#this is for all the creation of the questions

#the questions home page
@app.route('/questions')
def about():

    conn = sqlite3.connect("SQL/questionDatabase.db")
    conn.row_factory = sqlite3.Row
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    
    return render_template('questions.html', posts=posts)

#modyfing the questions
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']

        if not question:
            flash('question is required!')
        else:
            conn = sqlite3.connect("SQL/questionDatabase.db")
            conn.row_factory = sqlite3.Row
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (question, answer))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('createQuestion.html')


@app.route('/question/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post = getQuestion(id)

    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']

        if not question:
            flash('question is required!')
        else:
            conn = sqlite3.connect("SQL/questionDatabase.db")
            conn.row_factory = sqlite3.Row
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (question, answer, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('editQuestion.html', post=post)

@app.route('/question/<int:id>/delete', methods=('POST',))
def delete(id):
    post = getQuestion(id)
    conn = sqlite3.connect("SQL/questionDatabase.db")
    conn.row_factory = sqlite3.Row
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))