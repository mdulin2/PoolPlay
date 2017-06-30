

#the definition of a single team
class Team:
    #initializer
    def __init__(self,name):
        self.__ID = name
        self.__games = 0
        self.__schedule = []

    #true if the game is in the schedule
    #false otherwise
    def hasGame(self,user,opp):
        if((user.getID(),opp.getID()) in self.__schedule
         or (opp.getID(),user.getID()) in self.__schedule):
            return True
        return False

    def getID(self):
        return self.__ID

    def getGames(self):
        return self.__games

    def addGame(self,user,opp):
        self.__games +=1
        self.__schedule.append((user.getID(),opp.getID()))

    def printSchedule(self):
        print self.__schedule

#a singlar games information
class Game:
    def __init__(self,gameNumber):
        self.__gameID = gameNumber
        self.__user = 0
        self.__opponent = 0

    #returns who the user of the game is
    def getUser(self):
        return self.user

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
                if(self.__teamList[i].hasGame(self.__teamList[i],
                self.__teamList[opp]) == False and i != opp):
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
                if(self.__teamList[i].hasGame(self.__teamList[i],
                self.__teamList[opp]) == False and i != opp):
                    #testing if the opponent has too many games
                    if(self.__teamList[opp].getGames() < self.__maxGames):
                        self.addGame(i,opp)

                #moving up the opponent
                opp = (opp+1)%self.__teams
                if(opp == i):
                    break

        self.__maxGames = self.__maxGames + 1

    #print each schedule out for the teams
    def printAllSchedules(self):
        for i in range(len(self.__teamList)):
            print "Team ",self.__teamList[i].getID()," ",
            self.__teamList[i].printSchedule()


    #gets the teams from the schedule
    def getTeams(self):
        return self.__teamList

    #returns the number of teams in the pool
    def getTeamCount(self):
        return self.__teams

#creates seperate pools to form a pool play tournament
class Bracket:

    def __init__(self):
        self.poolBracket = {}
        self.__teams = 0
        self.__games = 0
        self.__pools = 0

    #creates the full amount of pool play brackets
    #games: amount of games to be played per team, minimum
    #teams: the amount of teams in the tournament
    #pools: The amount of pools
    def makeBracket(self,games,teams,pools):
        self.__teams = teams
        self.__games = games
        self.__pools = pools
        self.__insertPools()

    #displays each pool with their respected games
    def printPools(self):
        for i in range(self.__pools):
            print "Pools ", i+1
            self.poolBracket[i+1].printAllSchedules()

    #inserts the pools into the dictionary
    def __insertPools(self):
        teamCount = 1
        interval = self.__getTeamLst(0)
        for i in range(self.__pools):
            tmpPool = Pool()
            tmpPool.createSchedule(self.__games,interval[i],teamCount)
            self.poolBracket[i+1] = tmpPool
            teamCount += interval[i]

    #cretes the amount of teams that is going to be in each pool
    #returns a lst full of numbers, which are teams in each pool.
    def __getTeamLst(self,div):
        lst = []
        interval =( self.__teams + div)/self.__pools

        #rounding down
        if((self.__teams + div) % self.__pools == 0):

            for i in range(self.__pools):
                if(i + div >= self.__pools):
                    lst.append(interval - 1)
                else:
                    lst.append(interval)
            print lst
            return lst

        #rounding up
        elif((self.__teams -div)% self.__pools == 0):
            for i in range(self.__pools):
                if(i + div >= self.__pools):
                    lst.append(interval + 1)
                else:
                    lst.append(interval)
            print lst
            return lst
        #if going "div" up or down doesn't create the correct number of teams per pool
        else:
            return self.__getTeamLst(div+1)

if(__name__ == "__main__"):

    B = Bracket()
    B.makeBracket(3,18,4)
    B.printPools()
    #B.createPools(7,16,3)
    #B.printBrackets()