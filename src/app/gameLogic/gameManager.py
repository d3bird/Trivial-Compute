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
    
    def playerLeaveGame(self, playerID, gameID):
        print("player : " + str(playerID) + " is leaving game " + str(gameID))