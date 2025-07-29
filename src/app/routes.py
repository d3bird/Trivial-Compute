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
from werkzeug.exceptions import abort
import app.gameLogic.gameData as gameData
from flask_sock import Sock
from flask_socketio import SocketIO, emit
import random 
from datetime import datetime
from threading import Lock
import os
from app import app, sock, socketio
from app import allGames,  UPLOAD_FOLDER, ALLOWED_EXTENSIONS, QuestionDB

from app.forms import LoginForm

thread = None
thread_lock = Lock()

def create_current_player_data():
    output =gameData.createPlayer()
    output['name'] = current_user.username
    output['SQL_ID'] = current_user.id
    output['valid'] = True
    return output

#-----------this is an example of an one time comunication between the sever and the client-------------
@app.route('/echoPage')
def echopage():
    return render_template('echo.html')

@sock.route('/echo')
def echo(sock):
    while True:
        data = sock.receive()
        sock.send(data)

@sock.route('/requestNewQuestion')
def requestNewQuestion(sock):
    gameId = 0
    print("getting new question, and sending it ")
    allGames.getGameInfo(gameId)['need_newQuestion'] = True
    while True:
        data = sock.receive()
        sock.send(data)


#this needs to be a better solution than to have one for every question type
@sock.route('/selectAnswer1')
def selectAnswer1(sock):
    gameId = 0
    print("selecting answer1 (right)")

    
    current_player_data = create_current_player_data()
    allGames.increasePlayerRight(gameId, current_player_data)

    #allGames.getGameInfo(gameId)['need_newQuestion'] = True
    while True:
        data = sock.receive()
        sock.send(data)

@sock.route('/selectAnswer2')
def selectAnswer2(sock):
    gameId = 0
    print("selecting answer2 (wrong)")
    current_player_data = create_current_player_data()
    allGames.increasePlayerWrong(gameId, current_player_data)
    #allGames.getGameInfo(gameId)['need_newQuestion'] = True
    while True:
        data = sock.receive()
        sock.send(data)

@sock.route('/selectAnswer3')
def selectAnswer3(sock):
    gameId = 0
    print("selecting answer3 (wrong)")
    current_player_data = create_current_player_data()
    allGames.increasePlayerWrong(gameId, current_player_data)
    #allGames.getGameInfo(gameId)['need_newQuestion'] = True
    while True:
        data = sock.receive()
        sock.send(data)

@sock.route('/rollDice')
def rollDice(sock):
    gameId = 0
    print("selecting answer1 (right)")

    
    current_player_data = create_current_player_data()
    allGames.rollDice(gameId, current_player_data)
    #allGames.getGameInfo(gameId)['need_newQuestion'] = True

    #allGames.getGameInfo(gameId)['need_newQuestion'] = True
    while True:
        data = sock.receive()
        sock.send(data)

#-------------------------------these are the functions for the constant comunication---------------------
"""
Get current date time
"""
def get_current_datetime():
    now = datetime.now()
    return now.strftime("%m/%d/%Y %H:%M:%S")

"""
Generate random sequence of dummy sensor values and send it to our clients
"""
def background_thread():
    print("starting background thread to update clients when someone has joined")
    while True:
        dummy_sensor_value = round(random.random() * 100, 3)
        socketio.emit('updateSensorData', {'value': dummy_sensor_value, "date": get_current_datetime()})

        

        socketio.sleep(1)

def game_background_thread():
    print("starting background thread to update clients when someone has joined")
    gameId = 0
    while True:
        player_data = allGames.getGameInfo(gameId)['players']
        need_new_question = allGames.getGameInfo(gameId)['need_newQuestion']
        print("sending player data")
        for player_key in player_data.keys():
            player = player_data[player_key]
            row_num = player['playerID']
            username = player['name']
            sql_id = player['SQL_ID']
            right = player['questionGottenRight']
            wrong = player['questionGottenWrong']

            socketio.emit('updatePlayerData', {'row_num': row_num, "username": username, "sql_id": sql_id,"right": right,"wrong": wrong})

        if need_new_question:
            questionData = QuestionDB.getRandomQuestion()
            answers =  str(questionData['content']).split(',')
            print(str(questionData['content']))
            print("THEY NEED A NEW QUESTION")
            question = questionData['title']
            #only doing the first 3 answers to show that the system is working
            answer1 = answers[1]
            answer2 = answers[2]
            answer3 = answers[3]
            socketio.emit('newQuestion', {'question': question, "answer1": answer1, "answer2": answer2, "answer3": answer3})
            allGames.getGameInfo(gameId)['need_newQuestion'] = False


        socketio.sleep(1)

"""
Serve root index file
"""
@app.route('/constRandom')
def constRandom():
    return render_template('constRandom.html')

"""
Decorator for connect
"""
@socketio.on('connect')
def connect():
    global thread
    print('Client connected')

    global thread
    with thread_lock:
        if thread is None:
            thread = socketio.start_background_task(game_background_thread)

"""
Decorator for disconnect
"""
@socketio.on('disconnect')
def disconnect():
    print('Client disconnected',  request.sid)
    current_player_data = create_current_player_data()
    allGames.discounectPlayerFromEveryGame(current_player_data)

#---------------------------------------------------------------------------------------------------------------

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
def join(id):
    gameInfo = allGames.getGameInfo(id)

    if gameInfo == None:
        print("tried to join a game that did not exist")
        abort(404)
    current_player_data = create_current_player_data()
    joinWork = allGames.playerJoinGame(current_player_data, id)
    if joinWork == False:
        return redirect(url_for('index'))

    gameInfo = allGames.getGameInfo(id)
    #generate the inforamtion for the table headers
    headers = ("username" ,"player ID", "player number", "questions wrong", "questions right")

    catagory_headers = ("color" ,"catagory number", "catagory name")
    
    catagory_data = []
    red_data    = ("red" ,"0", "none given")
    catagory_data.append(red_data)

    green_data  = ("green" ,"1", "none given")
    catagory_data.append(green_data)

    blue_data   = ("blue" ,"2", "none given")
    catagory_data.append(blue_data)

    yellow_data = ("yello" ,"3", "none given")
    catagory_data.append(yellow_data)
    
    #get the inforamtion from the games
    data = []
    counter = 0
    for player_key in gameInfo['players'].keys():
        player = gameInfo['players'][player_key]
        username = "empty_spot"
        ID = "-1"
        questions_wrong = -1
        questions_right = -1
        if player['valid']:
            username = str(player['name'])
            ID = str(player['SQL_ID'])
            questions_wrong = str(player['questionGottenWrong'])
            questions_right = str(player['questionGottenRight'])
        gameData = [username, ID, counter, questions_wrong, questions_right]
        counter += 1
        data.append(gameData)
    
    #to get the table to display correctly, needed to use the tuple data type
    #there is probably better ways to do this but this will work for now
    data = tuple(tuple(item) for item in data)
    print(str(data))
    return render_template('gameLobby.html', headers=headers, data=data, catagory_headers=catagory_headers, catagory_data=catagory_data)

#-----------------------game logic----------------------------------------
#TODO: implement frontend socket to handle clicking dice, picking square, and answering question

@socketio.on('roll_die')
def roll_die(id):
    game = allGames.getGameInfo(id)['logicObject'].game
    roll = random.randint(1, 6)
    emit('dice_rolled', {'roll': roll})
    emit('moves', game.moves(roll))

@socketio.on('pick_square')
def move(id, sq):
    game = allGames.getGameInfo(id)['logicObject'].game
    game.move_to(sq)
    cat = sq.category
    #TODO: implement categories
    emit('question', QuestionDB.getRandomQuestion())

@socketio.on('answer')
def answer(id, is_correct):
    game = allGames.getGameInfo(id)['logicObject'].game
    if is_correct:
        winner = game.update_correct()
        #TODO: game end logic
        if winner:
            allGames.end_game(id)
    else:
        game.next_turn()


@app.route('/game', methods=('GET', 'POST'))
def gamePage():
    print("player loaded game page")
    return render_template('game.html')

#-----------------------misc pages----------------------------------------
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/howToPlay')
def howToPlay():
    return render_template('howToPlay.html')

#--------------------------modifying questions----------------------------


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
    #flash('"{}" was successfully deleted!'.format(post['title']))
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
            #chck to makesure teh output dir exists
            if os.path.isdir(app.config['UPLOAD_FOLDER']) == False:
                os.mkdir(app.config['UPLOAD_FOLDER'])
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('download_file', name=filename))
            return redirect(url_for('questions'))
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''