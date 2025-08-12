from app.gameLogic.board import Board, Square
import random
class gameLogic:
    def __init__(self, gameID, players):
        self.gameID = gameID
        self.board = Board()
        self.players = players
        
        self.turn_order = []
        self.turn_order_index = 0

        self.currentPlayer_ID = 0

        self.current_players_turn = -1 # is the player ID to get from players
        self.current_turn_over = False
        self.current_movement_left = 0
        self.last_roll = 0

        self.need_to_send_roll = False

        self.game_started = False

        #inforamtion about the current question 
        self.need_to_send_question = False
        self.need_to_answer = False
        self.correct_answer = False
        self.isCurrentSpot_HQ = False
        self.isCurrentSpot_color = ""

        #this tells the game what to do  since each one of the functions changes the state
        #has to be done like this because the main loop is rest based
        #can be : 
        # game_start : waiting for enough players
        # rolling   : waiting for the player to roll the dice
        # moving   : waiting for the player to roll the dice
        # pick_dir   : waiting for the player to picka direction
        # question  : waiting for the player to answer the question
        # endTurn   : starting next turn, checking to see if the game is over
        #victory    :end of teh game has come
        self.current_state = "game_start"

        self.last_gui_state = 0

    def get_expected_gui_state(self):
        if str(self.current_state) == "game_start":
            return 0
        if str(self.current_state) == "rolling":
            return 4
        if str(self.current_state) == "moving":
            return 1
        if str(self.current_state) == "pick_dir":
            return 3
        if str(self.current_state) == "question":
            return 2
        if str(self.current_state) == "endTurn":
            return 2

    def start_game(self):
        if self.game_started == False:
            self.start_next_turn()
        self.game_started = True

    def start_next_turn(self):
        print("self.turn_order_index " + str(self.turn_order_index))
        print("len(self.turn_order) " + str(len(self.players.keys())))
        self.current_turn_over = False
        #checks to makesure that it is not the first turn before updating the index
        if self.current_players_turn != -1:
            #get the next player's turn
            self.turn_order_index += 1 
            self.currentPlayer_ID += 1 
            if self.turn_order_index >= len(self.players.keys()):
                self.turn_order_index = 0
                self.currentPlayer_ID = 0
        self.current_players_turn = self.turn_order_index
        self.current_movement_left = 0
        self.current_state = "rolling"

    def rollDice(self):
        roll = random.randint(1,6) 
        print("rolling dice for player, they got " + str(roll))
        self.current_movement_left = roll
        self.last_roll = roll
        self.current_state  = "moving"
        self.need_to_send_roll = True
        return roll

    def move_one_square(self):
        #square_ID = self.players[self.current_players_turn]['square_currently_on']
        current_square = self.get_current_square()
        self.current_movement_left -= 1

        if self.current_movement_left <= 0:
            self.current_state  = "question"
            self.need_to_answer = True
            self.need_to_send_question = True
            self.need_to_send_roll = False
        #is there a direction to turn
        #if there are 3 options then 
        elif len(current_square.get_neighbors()) > 2:
            self.current_state  = "pick_dir"

    def answer(self, correct):
        print("cool")
        self.need_to_send_question = False
        self.need_to_answer = False
        self.correct_answer = correct
        if self.isCurrentSpot_HQ and correct:
            self.award_wedges(self.currentPlayer_ID, self.isCurrentSpot_color)
        
    def is_turn_over(self):
        return self.current_turn_over

    def get_player_square(self, playerID):
        square = None
        if str(playerID) in self.players.keys():
            space = self.players[str(playerID)]['square_currently_on']
            square = self.board.get_square(space)
            print("square data : " +str(square))
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

    def update_game(self, client_updates):
        data = {}
        data['move_amount_left'] = 0
        data['last_roll'] = self.last_roll
        data['need_to_roll_again'] = False
        data['need_to_choose_direction'] = False
        data['need_to_answer_question'] = False
        data['need_to_send_question'] = False
        data['endgame'] = False
        data['winner'] = 0

        print("the game is being updated")
        if str(self.current_state) == "rolling":
            print("waiting for dice roll")
        elif str(self.current_state) == "moving":
            data['move_amount_left'] = self.current_movement_left 
            self.move_one_square()
        elif str(self.current_state) == "question":
            data['need_to_answer_question'] = self.need_to_answer
            data['need_to_send_question'] = self.need_to_send_question

            #the question was answered
            if self.need_to_answer == False:
                endGame = self.check_if_game_is_over()
                if endGame != None:
                    data['endgame'] = True
                    data['winner'] = endGame
                    self.current_state = "victory"
                elif self.correct_answer == True:
                    self.current_state = "rolling"
                else:
                    self.current_state = "endTurn"
        elif str(self.current_state) == "endTurn":
            self.start_next_turn()
                
        data['player_turn'] = self.currentPlayer_ID
        data['gui_state'] = self.get_expected_gui_state()
        data['need_state_update'] = False
        if self.last_gui_state != data['gui_state']:
            data['need_state_update'] = True
        return data