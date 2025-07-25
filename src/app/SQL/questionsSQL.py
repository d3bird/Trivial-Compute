import os
import sqlite3
import random

class questionDB:
    def __init__(self, location = "app/SQL/schema"):
        self.DBName = "questionDatabase.db"
        self.location = location
        if self.doesDBExist() == False:
            self.createNewDataBase()

    def createNewDataBase(self):
        print("creating new question DB")
        connection = sqlite3.connect(self.DBName)

        print(str(os.getcwd()))

        schemaDir = self.location

        with open(schemaDir +'/buildDB.sql') as f:
            connection.executescript(f.read())

        cur = connection.cursor()
        
        inputQuestionCsv = "../questionSets/basicquestions.csv"
        with open(inputQuestionCsv, 'r') as file:
            skipFirstLine = True
            for line in file:
                if skipFirstLine:
                    skipFirstLine = False
                else:
                    rowData = line.split(',')
                    questionString = rowData[2]
                    answers = "catagory=" +rowData[1] 
                    for elm in rowData[3:]:
                        answers += ("," + elm)
                    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                                (questionString, answers)
                                )

                    #cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                    #            ('Second Post', 'Content for the second post')
                    #            )

        connection.commit()
        connection.close()

    def getNameofDataBase(self):
        return self.DBName

    def doesDBExist(self):
        name = self.getNameofDataBase()
        return os.path.isfile(name)

    def connectToDataBase(self):
        output = None
        if self.doesDBExist():
            output = sqlite3.connect(self.DBName)
        return output
    
    def getQuestion(self, post_id):
        conn = sqlite3.connect(self.DBName)
        conn.row_factory = sqlite3.Row
        post = conn.execute('SELECT * FROM posts WHERE id = ?',
                            (post_id,)).fetchone()
        conn.close()
        return post
    
    def getAllQuestions(self):
        conn = sqlite3.connect(self.DBName)
        conn.row_factory = sqlite3.Row
        questions = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        return questions
    
    def getRandomQuestion(self):
        conn = sqlite3.connect(self.DBName)
        conn.row_factory = sqlite3.Row
        questions = conn.execute('SELECT * FROM posts').fetchall()
        conn.close()
        start = 0
        end = len(questions) -1
        index = random.randint(start, end)
        return questions[index]

    def createQuestion(self, question, answer):
        conn = sqlite3.connect(self.DBName)
        conn.row_factory = sqlite3.Row
        conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (question, answer))
        conn.commit()
        conn.close()

    def editQuestion(self, id, question, answer):
        conn = sqlite3.connect(self.DBName)
        conn.row_factory = sqlite3.Row
        conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (question, answer, id))
        conn.commit()
        conn.close()

    def deleteQiestion(self, id):
        conn = sqlite3.connect(self.DBName)
        conn.row_factory = sqlite3.Row
        conn.execute('DELETE FROM posts WHERE id = ?', (id,))
        conn.commit()
        conn.close()