from app.gameLogic.board import Board, Square
from app.gameLogic.player import Player
# from random import randint
# from app import QuestionDB

class Game:
    def __init__(self, players=None):
        self.board = Board()
        self.players = []
        if players:
            for playerID in players:
                self.players.append(Player(id=playerID, start=self.board.start))
        self.curr = 0

    def moves(self, n):
        player = self.players[self.curr]
        return player.square.moves(n)
        
    def move_to(self, sq):
        player = self.players[self.curr]
        player.move(sq)

    def next_turn(self):
        self.curr = (self.curr + 1) % len(self.players)

    def update_correct(self):
        player = self.players[self.curr]
        if player.square.hq:
            player.chips[player.square.category] = True
        elif player.square.center and all(player.chips):
            return player.id


    # def turn(self):
    #     player = self.players[self.curr]
    #     while True:
    #         die = randint(1, 6)
    #         moves = player.square.moves(die)
    #         # TODO: player picks move
    #         player.square = moves[0]
    #         if player.square.roll_again:
    #             continue
    #         if player.square.center:
    #             # TODO: choose category
    #             category = 0
    #         else:
    #             category = player.square.category
    #         _, _, question, answer = QuestionDB.getRandomQuestion()
    #         print(question)
    #         response = input("Answer: ")
    #         if response == answer:
    #             if player.square.hq:
    #                 player.chips[category] = True
    #             elif player.square.center and all(player.chips):
    #                 print("You win!")
    #                 return
    #         else:
    #             break

    #     self.curr = (self.curr + 1) % len(self.players)
