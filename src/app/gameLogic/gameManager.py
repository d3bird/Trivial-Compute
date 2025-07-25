import app.gameLogic.gameData as gameData

class gameMaster:
    def __init__(self, numOfServers):
        self.games = {}
        
        self.lobbySize = 4

        #create all the games to handle
        counter = 0
        while counter < numOfServers:
            self.games[str(counter)] = gameData.createNewGame(counter, self.lobbySize )
            self.games[str(counter)]['logicObject'].startThread()
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
    
    def end_game(self, game_ID):
        self.games[str(game_ID)]['started'] = False

    def reset_game(self, game_ID):
        self.games[str(game_ID)] = gameData.createNewGame()

    def increasePlayerRight(self, gameID, playerData ):
        player_data = self.getGameInfo(gameID)['players']
        for player_key in player_data.keys():
            player = player_data[player_key]
            if str(player['name']) == str(playerData['name']):
                print("setting user answer wrong")
                self.getGameInfo(gameID)['players'][player_key]['questionGottenRight'] +=1

    def increasePlayerWrong(self, gameID, playerData ):
        player_data = self.getGameInfo(gameID)['players']
        for player_key in player_data.keys():
            player = player_data[player_key]
            if str(player['name']) == str(playerData['name']):
                print("setting user answer wrong")
                self.getGameInfo(gameID)['players'][player_key]['questionGottenWrong'] +=1


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

    