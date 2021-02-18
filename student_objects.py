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
    """
    Class object to store a student's infomation such a desired graduation date,
    if they are willing to take classes over the summer, and what courses they
    completed
    """

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
        """
        Function for removing a degree from the student.degree_list

        Inputs:
            degree_name - (str) the name of the degree to be removed

        Returns:
            None
        """
        pass

    def add_course(self, course_name: str, year: str, term: int):
        """
        Function add a course object into self.student plan with position being
        determined by inputed "year" and "term"

        Inputs:
            course_name -
            year -
            term -

        """
        added_course = None
        #get course object that coresponds to the inputed course_name
        for course in self.degree_list:
            if course.name == course_name:
                added_course = course
                break

        #add course object into self.plan
        self.plan[year][term].append(course)

    def remove_course(self, course_name: str, year: str, term: int):
        """
        Function remove a course object from self.student plan with position
        being determined by inputed "year" and "term"

        Inputs:
            course_name -
            year -
            term -

        """

        #check to confirm course is in self.plan
        course_found = False
        for course in self.plan[year][term]:
            if course.name == course_name:
                course_found = True
                self.plan[year][term].remove(course)

        if course_found == False:
            print("Error")

    def generate_plan(self):

        #create copy of self.plan

        #add cources to plan_copy untill all requirements have been met

        #return course copy

    def checkcompetion(self):
        """
        check if all degrees for the student has had their requirments met
        """
        pass
