from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import app.gameLogic.gameManager 
import app.SQL.questionsSQL
from flask_socketio import SocketIO
from flask_sock import Sock

#the end goal is to have 10 severs, but for testing have only one 
#allGames = app.gameLogic.gameManager.gameMaster(10)
allGames = app.gameLogic.gameManager.gameMaster(1)

QuestionDB = app.SQL.questionsSQL.questionDB()


app = Flask(__name__)
app.config.from_object(Config)
socketio = SocketIO(app)
sock = Sock(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
UPLOAD_FOLDER = './uploadedFiles'
ALLOWED_EXTENSIONS = {'txt', 'json', 'csv'}

from app import routes, models, eventHandler

