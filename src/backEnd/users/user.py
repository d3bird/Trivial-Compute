

class user:
    def __init__(self, name, password):
        self.name = name 
        self.password = password
        self.loggedIn = False

    def login(self):
        self.loggedIn = True

    def logout(self):
        self.loggedIn = False

    def isLoggedIn(self):
        return self.loggedIn

    def confirmPassword(self,input):
        return self.password == input
    
    def resetPassword(self,input):
        self.password == input