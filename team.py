from game import Game
#the definition of a single team
class Team:
    #initializer
    def __init__(self,name):
        self.__ID = name
        self.__games = 0
        self.__schedule = []

    #true if the game is in the schedule
    #false otherwise
    def hasGame(self,opp):
        for game in self.__schedule:
            if(game.getOpp() == opp.getID()):
                return True
        return False

        if((user.getID(),opp.getID()) in self.__schedule
         or (opp.getID(),user.getID()) in self.__schedule):
            return True
        return False

    #returns the team's ID
    def getID(self):
        return self.__ID

    #returns the number of games a team has played
    def getGames(self):
        return self.__games



    #adds a game to the team's schedule
    #user: the team being added
    #opp: the oppoenent team being added
    def addGame(self,game,opp):
        self.__games +=1
        newGame = Game(self.__ID,opp.getID())
        self.__schedule.append(newGame)

    #prints out the schedule for a team
    def printSchedule(self):
        for game in self.__schedule:
            game.printGame()
        print

    def getSchedule(self):
        return self.__schedule
