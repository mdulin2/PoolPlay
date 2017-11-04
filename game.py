
#a singlar games information
class Game:
    def __init__(self,user,opponent):
        self.__gameID = 0
        self.__user = user
        self.__opponent = opponent

    #returns who the user of the game is
    def getUser(self):
        return self.__user

    #returns who the opponent of the game is
    def getOpp(self):
        return self.__opponent

    #returns the game number
    def getGameID(self):
        return self.__gameID

    #sets the user for the game
    def setUser(self,user):
        self.__user = user

    #sets the opponent of the game
    def setOpp(self,opp):
        self.__opponent = opp

    def printGame(self):
        print "| ",self.__user, " vs ",self.__opponent, " | ",
