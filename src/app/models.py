from datetime import datetime, timezone
from werkzeug.security import generate_password_hash, check_password_hash
from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from flask_login import UserMixin
from app import login


class User(UserMixin,db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True,
                                                unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    game_count: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    wrongAnswer_count: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    rightAnswer_count: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))
    gamesWon_count: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))


    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def increment_wrong_answers(self):
        self.wrongAnswer_count = int(self.wrongAnswer_count) + 1

    def increment_right_answers(self):
        self.rightAnswer_count = int(self.rightAnswer_count) + 1
        
    def increment_games_played(self):
        self.game_count = int(self.game_count) + 1

    def increment_games_won(self):
        self.gamesWon_count = int(self.gamesWon_count) + 1

    
@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))