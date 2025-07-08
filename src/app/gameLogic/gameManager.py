import app.gameLogic.gameData as gameData

class gameMaster:
    def __init__(self, numOfServers):
        self.games = {}
        
        self.lobbySize = 4

        #create all the games to handle
        counter = 0
        while counter < numOfServers:
            self.games[str(counter)] = gameData.createNewGame(counter, self.lobbySize )
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

    def playerJoinGame(self, playerID, gameID):
        print("player : " + str(playerID) + " is joining game " + str(gameID))

    
    def playerLeaveGame(self, playerID, gameID):
        print("player : " + str(playerID) + " is leaving game " + str(gameID))