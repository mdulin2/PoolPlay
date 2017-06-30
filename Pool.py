import Bracket
import Team



#the class that makes the schedule
class Pool:
    def __init__(self):
        self.teams = 0
        self.games = 0
        self.maxGames = 1
        self.startingP = 0
        self.teamList = []


    #initializes the teams
    def initTeams(self,teamCount):
        self.teamList = []
        self.teams = teamCount
        for i in range(self.startingP,teamCount + self.startingP):
            newTeam = Team(i)
            self.teamList.append(newTeam)


    #creates the schedule for the tournament
    #games: amount of games to be played by each team
    #Note**: the games are a minimum, not a maxiumum
    #teamCount:number of teams to have games
    def createSchedule(self,games,teamCount,startingPoint):
        self.games = games
        self.startingP = startingPoint
        self.initTeams(teamCount)
        for i in range(self.games):
            self.addRound()

        self.addLastRound()

    #adds the last round of the pool
    #fixes any issues inside of the pools
    def addLastRound(self):
        opp = 1
        #all teams get a game
        for i in range(self.teams):
            opp = (i+1)%self.teams

            #make sure that i doesn't have too many games
            while(self.teamList[i].getGames() < self.maxGames-1):
                #testing if the game is doable
                if(self.teamList[i].hasGame(self.teamList[i],
                self.teamList[opp]) == False and i != opp):
                    #testing if the opponent has too many games
                    if(self.teamList[opp].getGames() < self.maxGames+1):
                        self.addGame(i,opp)

                #moving up the opponent if it's not there for the round
                opp = (opp+1)%self.teams
                if(opp == i):
                    break

    #adds a singular game to both teams schedules
    #user and opp are the teams being added
    def addGame(self,user,opp):
        self.teamList[user].addGame(self.teamList[user],self.teamList[opp])
        self.teamList[opp].addGame(self.teamList[opp],self.teamList[user])

    #adds a single game to each team
    def addRound(self):
        opp = 1

        #all teams get a game
        for i in range(self.teams):
            opp = (i+1)%self.teams

            #make sure that i doesn't have too many games
            while(self.teamList[i].getGames() < self.maxGames):
                #testing if the game is doable
                if(self.teamList[i].hasGame(self.teamList[i],
                self.teamList[opp]) == False and i != opp):
                    #testing if the opponent has too many games
                    if(self.teamList[opp].getGames() < self.maxGames):
                        self.addGame(i,opp)

                #moving up the opponent
                opp = (opp+1)%self.teams
                if(opp == i):
                    break

        self.maxGames = self.maxGames + 1

    #print each schedule out for the teams
    def printAllSchedules(self,spot):
        for i in range(len(self.teamList)):
            print "Team ",spot+1," ",
            self.teamList[i].printSchedule()
            spot+=1
        return spot

    #gets the teams from the schedule
    def getTeams(self):
        return self.teamList
