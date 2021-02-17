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
    #need to figure out how we want to store degree (list or single degree object)

    def __init__(self,
                 identifier: str, 
                 summer = False,
                 desired_grad_date = ("Senior",3),
                 ):
        """
        Function to initialize Student class object

        Inputs:
            indicator - (str) student ID of student
            summer - (bool) a boolean indicator of whether or not the student is
                     willing to take courses over the summer (defaults to False)
            desired_grad_date - (tuple) a tuple in the form (year: str, term: int)
        """

        self.identifier = identifier
        self.degree_list = []
        self.plan = {"Freshman": [[], [], [], []],
                     "Sophomore": [[], [], [], []],
                     "Junior": [[], [], [], []],
                     "Senior": [[], [], [], []],
                     "Fifth": [[], [], [], []]
                     }
        self.summer = summer
        self.desired_grad_date = desired_grad_date

    def add_class_taken(self, course_name: str, year: str, term: int):
        """
        Function add a course object into self.student plan with position being
        determined by inputed "year" and "term"

        Inputs:

        """
        self.plan[year][term].append(cources_name)

    def add_class_planning(self, class_name: str, year: str, term: int):
        pass

    def remove_class(self, class_name: str, year: str, term: int):
        #need check to confirm class is in self.plan
        pass
