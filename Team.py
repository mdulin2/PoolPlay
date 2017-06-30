import Bracket
import Pool

#the definition of a single team
class Team:
    #initializer
    def __init__(self,name):
        self.ID = name
        self.games = 0
        self.schedule = []

    #true if the game is in the schedule
    #false otherwise
    def hasGame(self,user,opp):
        if((user.getID(),opp.getID()) in self.schedule
         or (opp.getID(),user.getID()) in self.schedule):
            return True
        return False

    def getID(self):
        return self.ID

    def getGames(self):
        return self.games

    def addGame(self,user,opp):
        self.games +=1
        self.schedule.append((user.getID(),opp.getID()))

    def printSchedule(self):
        print self.schedule

#a singlar games information
class Game:
    def __init__(self,gameNumber):
        self.gameID = gameNumber
        self.user = 0
        self.opponent = 0

    #returns who the user of the game is
    def getUser(self):
        return self.user

    #returns who the opponent of the game is
    def getOpp(self):
        self.opponent

    #returns the game number
    def getGameID(self):
        return self.gameID

    #sets the user for the game
    def setUser(self,user):
        self.user = user

    #sets the opponent of the game
    def setOpp(self,opp):
        self.opponent = opp
