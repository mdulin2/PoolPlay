import abc
from abc import ABCMeta

#This class is made in order to format and change the Bracket class to specifications
class FormatAbstract:
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
