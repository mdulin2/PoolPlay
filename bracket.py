from pool import Pool

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
