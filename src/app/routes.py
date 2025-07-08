from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user
import sqlalchemy as sa
from app import db
from app.forms import RegistrationForm
from app.models import User
from flask_login import login_required
from flask import request
from urllib.parse import urlsplit
from werkzeug.utils import secure_filename

import os
from app import app
from app import allGames,  UPLOAD_FOLDER, ALLOWED_EXTENSIONS, QuestionDB

from app.forms import LoginForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    game_count = 0
    if current_user.game_count != None:
        game_count = int(current_user.game_count)   

    wrongAnswer_count = 0 
    if current_user.wrongAnswer_count != None:
        wrongAnswer_count = int(current_user.wrongAnswer_count)

    rightAnswer_count = 0
    if current_user.rightAnswer_count != None:
        rightAnswer_count = int(current_user.rightAnswer_count)

    gamesWon_count = 0
    if current_user.gamesWon_count != None:
        gamesWon_count = int(current_user.gamesWon_count)

    #generate the inforamtion for the lobbies 

    #generate the inforamtion for the table headers
    headers = ("name" ,"players", "max player", "status")
    
    #get the inforamtion from the games
    data = []
    for game in allGames.get_game_list():
        
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

    return render_template("index.html", game_count=game_count,
                           wrongAnswer_count=wrongAnswer_count,
                           rightAnswer_count=rightAnswer_count,
                           gamesWon_count=gamesWon_count,
                           headers=headers, data=data )

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(
            sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlsplit(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        current_user.game_count = 0
        current_user.wrongAnswer_count = 0
        current_user.rightAnswer_count = 0
        current_user.gamesWon_count = 0
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

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

#def getQuestion(post_id):
#    conn = sqlite3.connect("SQL/questionDatabase.db")
#    conn.row_factory = sqlite3.Row
#    post = conn.execute('SELECT * FROM posts WHERE id = ?',
#                        (post_id,)).fetchone()
#    conn.close()
#    if post is None:
#        abort(404)
#    return post

@app.route('/question/<int:post_id>')
def post(post_id):
    post = QuestionDB.getQuestion(post_id)
    if post is None:
        abort(404)
    return render_template('single_question.html', post=post)

#this is for all the creation of the questions

#the questions home page
@app.route('/questions')
def questions():

    #conn = sqlite3.connect("SQL/questionDatabase.db")
    #conn.row_factory = sqlite3.Row
    #posts = conn.execute('SELECT * FROM posts').fetchall()
    #conn.close()
    
    posts = QuestionDB.getAllQuestions()
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
            #conn = sqlite3.connect("SQL/questionDatabase.db")
            #conn.row_factory = sqlite3.Row
            #conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
            #             (question, answer))
            #conn.commit()
            #conn.close()
            QuestionDB.createQuestion(question, answer)
            return redirect(url_for('questions'))

    return render_template('createQuestion.html')


@app.route('/question/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    post =  QuestionDB.getQuestion(id)

    if request.method == 'POST':
        question = request.form['question']
        answer = request.form['answer']

        if not question:
            flash('question is required!')
        else:
            QuestionDB.editQuestion(id, question, answer)

            #conn = sqlite3.connect("SQL/questionDatabase.db")
            #conn.row_factory = sqlite3.Row
            #conn.execute('UPDATE posts SET title = ?, content = ?'
            #             ' WHERE id = ?',
            #             (question, answer, id))
            #conn.commit()
            #conn.close()
            return redirect(url_for('index'))

    return render_template('editQuestion.html', post=post)

@app.route('/question/<int:id>/delete', methods=('POST',))
def delete(id):
    post = QuestionDB.deleteQiestion(id)
    #QuestionDB.deleteQiestion(id)
    #conn = sqlite3.connect("SQL/questionDatabase.db")
    #conn.row_factory = sqlite3.Row
    #conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    #conn.commit()
    #conn.close()
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