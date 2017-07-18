'''
Functionality:
Makes a pool play bracket or team schedule
'''
import abc
from abc import ABCMeta

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


#creates seperate pools to form a pool play tournament
class Bracket:

    def __init__(self):
        self.poolBracket = []
        self.__teams = 0
        self.__games = 0
        self.__pools = 0

    #returns a particular pool
    #poolNo: pool being selected
    def getPool(self,poolNo):
        return self.poolBracket[poolNo]

    #creates the full amount of pool play brackets
    #games: amount of games to be played per team, minimum
    #teams: the amount of teams in the tournament
    #pools: The amount of pools
    def makeBracket(self,games,teams,pools):
        self.__teams = teams
        self.__games = games
        self.__pools = pools
        self.__insertPools()

    #returns the number of teams in the bracket
    def getTeamCount(self):
        return self.__teams

    def getPoolCount(self):
        return self.__pools

    def getTeamCount(self):
        return self.__teams

    def getGameCount(self):
        return self.__games

    #displays each pool with their respected games
    def printPools(self):
        for i in range(self.__pools):
            print "Pools ", i+1
            self.poolBracket[i].printAllSchedules()

    #inserts the pools into the dictionary
    def __insertPools(self):
        teamCount = 1
        interval = self.__getTeamLst(0)
        for i in range(self.__pools):
            tmpPool = Pool()
            tmpPool.createSchedule(self.__games,interval[i],teamCount)
            self.poolBracket.append(tmpPool)
            teamCount += interval[i]

    #returns the complete schedule of the tournament without games being duplicated
    def getFullPoolSchedule(self):
        fullTournamentSchedule = []
        for pool in self.poolBracket:
            data = pool.allGames()
            for game in data:
                fullTournamentSchedule.append(game)
        return fullTournamentSchedule

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

#This class is made in order to format and change the Bracket class to specifications
class Format:
    __metaclass__ = ABCMeta
    def __init__(self):
        pass

    #display the tournament schedule of the bracket
    @abc.abstractmethod
    def printSchedule(self):
        pass

    #gets the tournament schedule
    @abc.abstractmethod
    def __tournamentSchedule__(self):
        pass

    #changes the team names of the specified bracket
    @abc.abstractmethod
    def __changeTeamName__(self,teamID,teamName):
        pass

    #outputs the information to a text file
    @abc.abstractmethod
    def __fileOutput__(self):
        pass

#subclass of Format
#This version can print out a whole schdule
class FormatBracket(Format):
    def __init__(self,bracket):
        self.poolsBracket = bracket
        self.tournamentBracket = self.poolsBracket.getFullPoolSchedule()
        self.nameLookup = {}
        self.__makeNameLookup()

    def __makeNameLookup(self):
        for i in range(self.poolsBracket.getTeamCount()):
            self.nameLookup[i+1] = i+1

    def __tournamentSchedule__(self):
        return self.tournamentBracket

   #prints a bracket with all games only once
    def printSchedule(self,typeP):
        if(typeP == "A"):
            for i in range(len(self.tournamentBracket)):
                if(i % 3 == 2):
                    print "|",
                    print self.nameLookup[self.tournamentBracket[i].getUser()]," vs ",
                    print self.nameLookup[self.tournamentBracket[i].getOpp()],
                    print "|"
                else:
                    print "|",
                    print self.nameLookup[self.tournamentBracket[i].getUser()]," vs ",
                    print self.nameLookup[self.tournamentBracket[i].getOpp()],
                    print "|",
        else:
            runnningTeamCount = 1
            for pool in range(self.poolsBracket.getPoolCount()):
                myPool = self.poolsBracket.getPool(pool)
                for team in range(myPool.getTeamCount()):
                    print "Team:",self.nameLookup[runnningTeamCount], " "
                    myTeam = myPool.getTeam(team)
                    schedule = myTeam.getSchedule()
                    for game in range(len(schedule)):
                        print " | ",self.nameLookup[schedule[game].getUser()], "vs",
                        print self.nameLookup[schedule[game].getOpp()],
                    runnningTeamCount +=1
                    print " |"


    #changes the name of the team specified
    #teamID: the current number of the team
    #teamName: the name that the number is getting changed too
    def __changeTeamName__(self,teamID,teamName):
        if(teamID in self.nameLookup):
            self.nameLookup[teamID] = teamName
            return

        for team in self.nameLookup:
            if(self.nameLookup[team] == teamID):
                self.nameLookup[team] = teamName
                return
        print "Team trying to be replaced is not valid"


    def __fileOutput__(self):
        pass

#the user interface of the software
class User:
    def __init__(self):
        self.tmpBracket = Bracket()
        self.formattedBracket = FormatBracket(self.tmpBracket)

    #the user interface for the user
    def beginning(self):
        into = 0
        while(into != 6):
            into = input("Options:\n"
            "1. Make New Bracket:\n"
            "2. Print Team Schedules:\n"
            "3. Print Tourament Schedule:\n"
            "4. Change a Team Name: \n"
            "5. End the Session\n")

            if(into == 1):
                self.useBracket()
            elif(into == 2):
                self.printSchedules(into)
            elif(into == 3):
                self.printSchedules(into)
            elif(into == 4):
                self.changeTeamName()


    #gets the data structures ready for output
    def output(self,fileType):
        if(fileType == "excel"):
            #add tabs to it
            pass


    #making a formatting bracket
    def useBracket(self):
        try:
            gamesNum = input("Number of games per team to play: ")
            teamsNum = input("Number of teams in the tournament: ")
            poolsNum = input("Number of pools in the tourament: ")
            self.tmpBracket.makeBracket(gamesNum,teamsNum,poolsNum)
            tmpFB = FormatBracket(self.tmpBracket)
            self.formattedBracket = tmpFB
        except:
            print "Please give a valid information."

    #changes the name of a team
    #teamNum: the team number to replace
    #teamName: The name that the team will be replaced to.
    def changeTeamName(self):
        teamNum = input("Enter the Team Number to change: ")
        teamName = str(raw_input("Please enter the Team Name: "))

        self.formattedBracket.__changeTeamName__(teamNum,teamName)

    #printType: 2 for Full Tournament Schedule
    #printType: 3 for Pools Schedule per Team
    #prints all of the Schedules
    def printSchedules(self,printType):
        if(printType == 2):
            print "Full Tournament Schedule: "
            self.formattedBracket.printSchedule("A")
            print
        elif(printType == 3):
            print "Pool Play for each Team:"
            self.formattedBracket.printSchedule("s")

if(__name__ == "__main__"):
    U = User()
    U.beginning()
