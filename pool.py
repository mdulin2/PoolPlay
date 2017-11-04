from game import Game
from team import Team

#the class that makes the schedule
class Pool:
    def __init__(self):
        self.__teams = 0
        self.__games = 0
        self.__maxGames = 1
        self.__startingP = 0
        self.__teamList = []


    #initializes the teams
    def __initTeams(self,teamCount):
        self.__teamList = []
        self.__teams = teamCount
        for i in range(self.__startingP,teamCount + self.__startingP):
            newTeam = Team(i)
            self.__teamList.append(newTeam)


    #creates the schedule for the tournament
    #games: amount of games to be played by each team
    #Note**: the games are a minimum, not a maxiumum
    #teamCount:number of teams to have games
    def createSchedule(self,games,teamCount,__startingPoint):
        self.__games = games
        self.__startingP = __startingPoint
        self.__initTeams(teamCount)
        for i in range(self.__games):
            self.__addRound()

        self.__addLastRound()

    #adds the last round of the pool
    #fixes any issues inside of the pools
    def __addLastRound(self):
        opp = 1
        #all teams get a game
        for i in range(self.__teams):
            opp = (i+1)%self.__teams

            #make sure that i doesn't have too many games
            while(self.__teamList[i].getGames() < self.__maxGames-1):
                #testing if the game is doable
                if(self.__teamList[i].hasGame(self.__teamList[opp]) == False and i != opp):
                    #testing if the opponent has too many games
                    if(self.__teamList[opp].getGames() < self.__maxGames+1):
                        self.addGame(i,opp)

                #moving up the opponent if it's not there for the round
                opp = (opp+1)%self.__teams
                if(opp == i):
                    break

    #adds a singular game to both teams schedules
    #user and opp are the teams being added
    def addGame(self,user,opp):
        self.__teamList[user].addGame(self.__teamList[user],self.__teamList[opp])
        self.__teamList[opp].addGame(self.__teamList[opp],self.__teamList[user])

    #adds a single game to each team
    def __addRound(self):
        opp = 1

        #all teams get a game
        for i in range(self.__teams):
            opp = (i+1)%self.__teams

            #make sure that i doesn't have too many games
            while(self.__teamList[i].getGames() < self.__maxGames):
                #testing if the game is doable
                if(self.__teamList[i].hasGame(self.__teamList[opp]) == False and i != opp):
                    #testing if the opponent has too many games
                    if(self.__teamList[opp].getGames() < self.__maxGames):
                        self.addGame(i,opp)

                #moving up the opponent if something else is wrong
                opp = (opp+1)%self.__teams
                if(opp == i):
                    break

        self.__maxGames = self.__maxGames + 1

    #print each schedule out for the teams
    def printAllSchedules(self):
        for i in range(len(self.__teamList)):
            print "Team ",self.__teamList[i].getID()," "
            self.__teamList[i].printSchedule()

    #prints out a single team schedule
    #teamNo: the team number being printed
    def printTeamSchedule(self,teamNo):
        print "Team ",self.__teamList[teamNo].getID()," ",
        self.__teamList[teamNo].printSchedule()
        print

    #gets the teams from the schedule
    def getTeam(self,num):
        return self.__teamList[num]

    #returns the number of teams in the pool
    def getTeamCount(self):
        return self.__teams


    #returns a full schdule of the whole tournament inside of a list of tuples
    def allGames(self):
        fullSchedule = []
        for team in self.__teamList:
            for game in team.getSchedule():
                if(self.inSchedule(game,fullSchedule)== True):
                    fullSchedule.append(game)

        return fullSchedule

    def inSchedule(self,game,schedule):
        for item in schedule:
            if(item.getUser() == game.getOpp() and item.getOpp() == game.getUser()):
                return False
        return True
