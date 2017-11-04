from formatAbstract import FormatAbstract
#subclass of Format
#This version can print out a whole schdule
class FormatBracket(FormatAbstract):
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
