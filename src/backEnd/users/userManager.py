import users.importUsers as importUsers
import users.user as user

class userMgr:
    def __init__(self):
        self.users = importUsers.import_users()

    #yes I know this is a hacky solution, it will be moved to 
    #the sql data base when I get the time
    def saveUsers(self):
        importUsers.export_users(self.users)

    def createNewUser(self, username, password):
        newUser = user(username, password)
        self.users[username] = newUser
        self.saveUsers()

    def isUsernameAdvalable(self, name ):
        if str(name) in self.users.keys():
            return False
        return True
    
    #reutrns true of the action worked as expected
    def loginUser(self, name, password):
        output = False
        #check to see if the account exists
        if self.isUsernameAdvalable(name) == False:
            if self.users[name].isLoggedIn() == False and self.users[name].confirmPassword(password):
                output = True
                self.users[name].login()
        return output
    
    #reutrns true of the action worked as expected
    def logoutUser(self, name):
        output = False
        #check to see if the account exists
        if self.isUsernameAdvalable(name) == False:
            if self.users[name].isLoggedIn():
                output = True
                self.users[name].logout()
        return output