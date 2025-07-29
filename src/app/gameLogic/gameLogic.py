from app.gameLogic.board import Board, Square
import random
class gameLogic:
    def __init__(self, gameID, players):
        self.gameID = gameID
        self.board = Board()
        self.players = players
        
        self.turn_order = []
        self.turn_order_index = 0

        self.current_players_turn = -1
        self.current_turn_over = False
        
        #this tells the game what to do  since each one of the functions changes the state
        #has to be done like this because the main loop is rest based
        #can be : 
        # game_start
        # rolling   : waiting for the player to roll the dice
        # moving   : waiting for the player to roll the dice
        # pick_dir   : waiting for the player to picka direction
        # question  : waiting for the player to answer the question
        # endTurn   : waiting for the player to answer the question
        self.current_state = "game_start"

    def get_waiting_state(self):
        return self.current_state

    def start_next_turn(self):
        self.current_turn_over = False
        #checks to makesure that it is not the first turn before updating the index
        if self.current_players_turn != -1:
            #get the next player's turn
            self.turn_order_index += 1 
            if self.turn_order_index >= len(self.turn_order):
                self.turn_order_index = 0
        self.current_players_turn = self.turn_order[self.turn_order_index]

        self.current_state = "rolling"

    def rollDice(self):
        roll = random.randint(1,6) 
        self.current_state  = "moving"
        return roll


    def is_turn_over(self):
        return self.current_turn_over

    def get_player_square(self, playerID):
        space = self.players[playerID]['square_currently_on']
        square = self.board.get_square(space)
        return square

    def award_wedges(self, playerID, color):
        self.players[playerID]['wedgesWon']['color'] = True

    def check_if_game_is_over(self):
        outputID = None
        for player_key in self.players.keys():
            if self.players[player_key]['wedgesWon']['yellow'] and self.players[player_key]['wedgesWon']['blue'] and self.players[player_key]['wedgesWon']['red'] and self.players[player_key]['wedgesWon']['green']:
                outputID = player_key
                break
        return outputID