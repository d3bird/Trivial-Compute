import app.gameLogic.gameData as gameData
from app.gameLogic.game import Game

class gameMaster:
    def __init__(self, numOfServers):
        self.games = {}
        
        self.lobbySize = 4

        #create all the games to handle
        counter = 0
        while counter < numOfServers:
            self.games[str(counter)] = gameData.createNewGame(counter, self.lobbySize )
            self.games[str(counter)]['logicObject']
            counter +=1

    def get_game_list(self):
        output = []
        for key in self.games.keys():
            output.append(self.games[key])
        return output
    
    def getGameInfo(self, id):
        output = None
        if str(id) in self.games.keys():
            output= self.games[str(id)]
        return output

    def start_game(self, game_ID):
        self.games[str(game_ID)]['started'] = True
        self.games[str(game_ID)]['logicObject'].start_game()
        #self.games[str(game_ID)]['logicObject'].game = Game(players=self.games[str(game_ID)]['players'].keys())
    
    def end_game(self, game_ID):
        self.games[str(game_ID)]['started'] = False

    def reset_game(self, game_ID):
        self.games[str(game_ID)] = gameData.createNewGame()

    def rollDice(self, gameID, playerData ):
        self.getGameInfo(gameID)['logicObject'].rollDice()


    def increasePlayerRight(self, gameID, playerData ):
        player_data = self.getGameInfo(gameID)['players']
        self.getGameInfo(gameID)['logicObject'].answer(True)
        for player_key in player_data.keys():
            player = player_data[player_key]
            if str(player['name']) == str(playerData['name']):
                print("setting user answer wrong")
                self.getGameInfo(gameID)['players'][player_key]['questionGottenRight'] +=1

    def increasePlayerWrong(self, gameID, playerData ):
        player_data = self.getGameInfo(gameID)['players']
        self.getGameInfo(gameID)['logicObject'].answer(False)
        for player_key in player_data.keys():
            player = player_data[player_key]
            if str(player['name']) == str(playerData['name']):
                print("setting user answer wrong")
                self.getGameInfo(gameID)['players'][player_key]['questionGottenWrong'] +=1

    def movePlayer(self, gameID, playerData, locdata ):
        player_data = self.getGameInfo(gameID)['players']
        for player_key in player_data.keys():
            player = player_data[player_key]
            if str(player['name']) == str(playerData['name']):
                print("moving player to new loc")
                tmp = locdata['data'].split(',')
                x = tmp[0]
                y = tmp[1]
                if x == '-1' or y == '-1':
                    print("bad cords was given")
                    return 
                self.getGameInfo(gameID)['players'][player_key]['xloc'] =x
                self.getGameInfo(gameID)['players'][player_key]['yloc'] =y
                self.getGameInfo(gameID)['players'][player_key]['sendUpdateLoc'] =True

    def playerJoinGame(self, playerData, gameID):
        print("player : " + str(playerData['name']) + " is joining game " + str(gameID))

        openSpot = None
        for player_key in self.games[str(gameID)]['players'].keys():
            if self.games[str(gameID)]['players'][player_key]['valid'] == False:
                openSpot = player_key
        
        if openSpot == None:
            print("there are no open spots in this game, rejecting join")
            return False
        
        playerData['playerID'] = openSpot
        self.games[str(gameID)]['players'][openSpot] = playerData
        return True

    def discounectPlayerFromEveryGame(self, playerData):
        print("disconnecting player from all games")
        for key in self.games.keys():
            self.playerLeaveGame(playerData, key)

    def playerLeaveGame(self, playerData, gameID):
        print("player : " + str(playerData['name']) + " is leaving game " + str(gameID))
        for player_key in self.games[str(gameID)]['players'].keys():
            if self.games[str(gameID)]['players'][player_key]['valid']:
                print("current player names : " + str(self.games[str(gameID)]['players'][player_key]['name']))
                if self.games[str(gameID)]['players'][player_key]['name'] == playerData['name']:
                    print("removing player from game")
                    self.games[str(gameID)]['players'][player_key] = gameData.createPlayer()

    