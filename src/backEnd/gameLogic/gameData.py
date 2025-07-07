import random

def createNewGame():
    output = {}
    players = {}
    players['player1'] = createPlayer()
    players['player2'] = createPlayer()
    players['player3'] = createPlayer()
    players['player4'] = createPlayer()

    output['turnOrder'] = []
    output['turnOrder'].append("player1")
    output['turnOrder'].append("player2")
    output['turnOrder'].append("player3")
    output['turnOrder'].append("player4")
    
    #random the turn order
    output['turnOrder'] = random.shuffle(output['turnOrder'])

    return output


def createPlayer():
    output = {}
    output['valid'] = False
    output['name'] = "guest"
    output['color'] = "grey"
    output['SQL_ID'] = -1
    output['questionGottenRight'] = 0
    output['questionGottenWrong'] = 0

    return output
