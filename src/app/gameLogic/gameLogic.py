from app.gameLogic.board import Board, Square
import random
class gameLogic:
    def __init__(self, gameID, players):
        self.gameID = gameID
        self.board = Board()
        self.players = players
        
        self.turn_order = []
        self.turn_order_index = 0

        self.current_players_turn = -1 # is the player ID to get from players
        self.current_turn_over = False
        self.current_movement_left = 0
        
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


    def start_next_turn(self):
        self.current_turn_over = False
        #checks to makesure that it is not the first turn before updating the index
        if self.current_players_turn != -1:
            #get the next player's turn
            self.turn_order_index += 1 
            if self.turn_order_index >= len(self.turn_order):
                self.turn_order_index = 0
        self.current_players_turn = self.turn_order[self.turn_order_index]
        self.current_movement_left = 0
        self.current_state = "rolling"

    def rollDice(self):
        roll = random.randint(1,6) 
        self.current_movement_left = roll
        self.current_state  = "moving"
        return roll

    def move(self):
        square_ID = self.players[self.current_players_turn]['square_currently_on']
        current_square = self.get_current_square()

        #is there a direction to turn
        #if there are 3 options then 
        if len(current_square.get_neighbors()) > 2:
            self.current_state  = "pick_dir"
        else:
            self.current_state  = "question"

    def answer_correct(self):
        print("cool")


    def is_turn_over(self):
        return self.current_turn_over

    def get_player_square(self, playerID):
        square = None
        if playerID in self.players.keys():
            space = self.players[playerID]['square_currently_on']
            square = self.board.get_square(space)
        else:
            print("cold not find player ID : " + str(playerID))
            print("options are " + str(self.players.keys()))

        return square

    def get_current_square(self):
        return self.get_player_square(self.current_players_turn)

    def award_wedges(self, playerID, color):
        self.players[playerID]['wedgesWon'][color] = True

    def check_if_game_is_over(self):
        outputID = None
        for player_key in self.players.keys():
            all_true = True
            for wedge in self.players[player_key]['wedgesWon'].keys():
                if self.players[player_key]['wedgesWon'][wedge] == False:
                    all_true = False
                    break
            if all_true:
                outputID = player_key
                break
        return outputID
    
    def get_players(self):
        return self.players 
    
    def get_waiting_state(self):
        return self.current_state
