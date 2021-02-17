"""
----------------------------------------------------------------------------------------
File for defining Student class object and a class for storing a list of students

Author - Noah Kruss
Group - TBD
Last Modified - 2/16/21
----------------------------------------------------------------------------------------
"""
from degree_objects import *

class Student_List():

    def __init__(self):

        self.students = []


class Student():

    def __init__(self, identifier: str):
        """
        """

        self.identifier = identifier
        self.plan = {"Freshman": [[], [], [], []],
                     "Sophomore": [[], [], [], []],
                     "Junior": [[], [], [], []],
                     "Senior": [[], [], [], []],
                     "Fifth": [[], [], [], []]
                     }

    def add_class_taken(self, class_name: str, year: str, term: int):
        pass

    def add_class_planning(self, class_name: str, year: str, term: int):
        pass
