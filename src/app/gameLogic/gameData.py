import random


def createNewGame(gameID, numPlayers =4 ):
    output = {}
    output['name'] = gameID
    output['gameID'] = gameID
    output['players'] = {}
    output['turnOrder'] = []

    if numPlayers < 1:
        numPlayers = 4

    output['maxPlayers'] = numPlayers
    output['connectedPlayers'] = 0
    output['status'] = "pre-game"

    counter = 0 
    while counter < numPlayers:
        playerID = "player" + str(counter)
        output['players'][str(playerID)] = createPlayer(playerID)
        output['turnOrder'].append(playerID)
        counter +=1
    
    #random the turn order
    output['turnOrder'] = random.shuffle(output['turnOrder'])

    output['started'] = False

    return output


def createPlayer( SQLID = None):
    output = {}
    output['valid'] = False
    output['name'] = "guest"
    output['color'] = "grey"
    output['playerID'] = "none"
    output['SQL_ID'] = -1
    output['questionGottenRight'] = 0
    output['questionGottenWrong'] = 0


    return output