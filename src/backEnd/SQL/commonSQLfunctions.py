import os
import sqlite3


def getNameofDataBase():
    return "questionDatabase.db"

def doesDBExist():
    name = getNameofDataBase()
    return os.path.isfile(name)

def connectToDataBase():
    output = None
    if doesDBExist():
        output = sqlite3.connect(getNameofDataBase())
    return output