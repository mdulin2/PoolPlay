from team import *
'''
Functionality:
Makes a pool play bracket or team schedule
'''
import abc
from abc import ABCMeta
from pool import Pool
from bracket import Bracket
from formatBracket import FormatBracket

#the user interface of the software
class User:
    def __init__(self):
        self.tmpBracket = Bracket()
        self.formattedBracket = FormatBracket(self.tmpBracket)

    #the user interface for the user
    def beginning(self):
        into = 0
        while(into != 5):
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
