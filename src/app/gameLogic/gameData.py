import random
import app.gameLogic.gameLogic as gameLogic

#these are all the updates from the client to update the game
def create_updateInforamtion():
    data = {}
    data['need_newQuestion'] = False
    data['need_to_send_roll'] = False
    data['last_roll'] = 0
    data['gui_state'] = 0
    data['send_gui_update'] = False
    return data

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
    
    output['client_inputs'] = create_updateInforamtion()

    counter = 0 
    while counter < numPlayers:
        playerID = (counter)
        output['players'][str(playerID)] = createPlayer(playerID)
        output['turnOrder'].append(playerID)
        counter +=1
    
    output['logicObject'] = gameLogic.gameLogic(gameID, output['players'])

    #random the turn order
    # output['turnOrder'] = random.shuffle(output['turnOrder'])

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

    output['square_currently_on'] = 22
    output['square_came_from'] = 22

    output['sendUpdateLoc'] = False
    output['xloc'] = 4
    output['yloc'] = 4
    
    output['current_turn'] = False

    output['wedgesWon'] = {}
    output['wedgesWon']['yellow'] = False
    output['wedgesWon']['blue'] = False
    output['wedgesWon']['red'] = False
    output['wedgesWon']['green'] = False

    output['wedgesUpdate'] = False

    return output