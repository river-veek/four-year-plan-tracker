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

        # list of degree objects in the case that a student has more than 1 major (or a minor)
        self.degree_list = []

        self.plan = {"First": [[], [], [], []],
                     "Second": [[], [], [], []],
                     "Third": [[], [], [], []],
                     "Fourth": [[], [], [], []],
                     "Fifth": [[], [], [], []]
                     } # first, second, etc refer to the year in the students college experience
        self.summer = summer
        self.desired_grad_date = desired_grad_date

    def add_degree(self, degree_obj: Degree):
        """
        Function for adding a degree from the student.degree_list

        Inputs:
            degree_obj - (Degree) the Degree object to be added

        Returns:
            None
        """

        self.degree_list.append(degree_obj)

    def remove_degree(self, degree_name: str):
        """
        Function for removing a degree from the student.degree_list

        Inputs:
            degree_name - (str) the name of the degree to be removed

        Returns:
            None
        """

        for degree in self.degree_list:
            if degree.name == degree_name:
                self.degree_list.remove(degree)

    def add_course(self, course_name: str, year: str, term: int):
        """
        Function add a course object into self.student plan with position being
        determined by inputed "year" and "term"

        Inputs:
            course_name - (str) identifier of the course to add
            year - (str) indicates the year in which to add the course in self.plan
            term - (int) indicats the term in which to add the course in self.plan

        """
        added_course = None

        #get course object that coresponds to the inputed course_name
        for degree in  self.degree_list:
        for course in degree:
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
            course_name - (str) identifier of the course to add
            year - (str) indicates the year in which to find the course in self.plan
            term - (int) indicats the term in which to find the course in self.plan

        """

        #check to confirm course is in self.plan
        course_found = False
        for course in self.plan[year][term]:
            if course.name == course_name:
                course_found = True
                self.plan[year][term].remove(course)

        if course_found == False:
            print("Error")

    def generate_plan(self, year: str, term: int):
        #TODO

        #create copy of self.plan
        forecast_plan = self.plan.copy()

        ###figure out which requirments have not been met and put them all in a list

        #initialize unmet_courses
        unmet_courses = []
        for degree in self.degree_list:

        #remove courses from unmet_courses if in student plan
        for key in self.plan:
            for term in self.plan[key]:
                for course in term:
                    if course in unmet_courses:
                        unmet_courses.remove(course)

        ###sort this list by pre_rec_nums

        ###figure out the number of terms remaining before the desired grad date

        ###based off this number determine number of courses that need to be taken per term

        ###loop through unmet list popping off the from of the list and adding to the plan

        return forecast_plan

    def checkcompetion(self):
        """
        check if all degrees for the student has had their requirments met
        """
        pass
