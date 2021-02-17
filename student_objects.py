"""
----------------------------------------------------------------------------------------
File for defining Student class object and a class for storing a list of students

Author - Noah Kruss
Group - TBD
Last Modified - 2/16/21
----------------------------------------------------------------------------------------
"""
from degree_objects import *

class Student():
    #need to figure out how we want to store degree (list or single degree object)

    def __init__(self,
                 identifier: str,
                 summer = False,
                 desired_grad_date = ("Senior", 2),
                 ):
        """
        Function to initialize Student class object

        Inputs:
            identifier - (str) student ID of student
            summer - (bool) a boolean indicator of whether or not the student is
                     willing to take courses over the summer (defaults to False)
            desired_grad_date - (tuple) a tuple in the form (year: str, term: int)
        """

        self.identifier = identifier
        self.degree_list = []
        self.plan = {"First": [[], [], [], []],
                     "Second": [[], [], [], []],
                     "Third": [[], [], [], []],
                     "Fourth": [[], [], [], []],
                     "Fifth": [[], [], [], []]
                     }
        self.summer = summer
        self.desired_grad_date = desired_grad_date

    def add_degree(self, degree_name: str):
        pass

    def remove_degree(self, degree_name: str):
        pass

    def add_course(self, course_name: str, year: str, term: int):
        """
        Function add a course object into self.student plan with position being
        determined by inputed "year" and "term"

        Inputs:

        """
        self.plan[year][term].append(course_name)

    def remove_course(self, cource_name: str, year: str, term: int):
        #need check to confirm cource is in self.plan
        pass

    def generate_plan(self):

        #create copy of self.plan

        #add cources to plan_copy untill all requirements have been met

        #return course copy

    def checkcompetion(self):
        """
        check if all degrees for the student has had their requirments met
        """
        pass
