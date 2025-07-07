from flask import Flask 
from flask import render_template
from flask import request
from flask import url_for
from flask import flash
from flask import redirect
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
import os
import sqlite3

from  gameLogic.gameManager import gameMaster

gameMaster = gameMaster(10)

UPLOAD_FOLDER = './uploadedFiles'
ALLOWED_EXTENSIONS = {'txt', 'json', 'csv'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'exampleSecretKey'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#----------------------joining a game--------------------------------------------
@app.route('/')
def index():

    #generate the inforamtion for the table headers
    headers = ("name" ,"players", "max player", "status")
    
    #get the inforamtion from teh games
    data = []
    for game in gameMaster.get_game_list():
        
        name = str(game['name'])
        connectedPlayers = str(game['connectedPlayers'])
        maxPlayers = str(game['maxPlayers'])
        status = "in lobby"
        if game['started']:
            status ="started"
        gameData = [name, connectedPlayers, maxPlayers, status]
        data.append(gameData)
    
    #to get the table to display correctly, needed to use the tuple data type
    #there is probably better ways to do this but this will work for now
    data = tuple(tuple(item) for item in data)
    
    return render_template('index.html', headers=headers, data=data )


@app.route('/gameLobby/<int:id>/', methods=('GET', 'POST'))
def join(gameID):

    return render_template('gameLobby.html')

#-----------------------misc pages----------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/howToPlay')
def howToPlay():
    return render_template('howToPlay.html')

#--------------------------modifying questions----------------------------

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
def questions():

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


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''