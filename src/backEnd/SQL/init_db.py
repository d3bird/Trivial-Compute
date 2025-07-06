import sqlite3
import commonSQLfunctions

def createNewDataBase():
    connection = commonSQLfunctions.connectToDataBase()

    schemaDir = "schema"

    with open(schemaDir +'/buildDB.sql') as f:
        connection.executescript(f.read())

    cur = connection.cursor()

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('First Post', 'Content for the first post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Second Post', 'Content for the second post')
                )

    connection.commit()
    connection.close()


def resetDataBase():
    print("TODO reset DB")

if __name__ == "__main__":
    if commonSQLfunctions.doesDBExist() == False:
        createNewDataBase()
    else:
        print("database already exist")
