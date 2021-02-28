"""
----------------------------------------------------------------------------------------
File for defining Student class object and a class for storing a list of students

Authors - JT Kashuba, Noah Kruss
Group - TBD
Last Modified - 2/22/21
----------------------------------------------------------------------------------------
"""
from degree_objects import *
from degree_planning import *

class Student():
    """
    Class object to store a student's infomation such a desired graduation date,
    if they are willing to take classes over the summer, and what courses they
    completed
    """

    def __init__(self,
                 identifier: str,
                 summer = False,
                 desired_grad_date = (4, 2),
                 max_credits_per_term = 12
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

        self.plan = {1: [[], [], [], []],
                     2: [[], [], [], []],
                     3: [[], [], [], []],
                     4: [[], [], [], []]
                     } # 1, 2, etc refer to the year in the students college experience
        self.courses_taken = []

        self.summer = summer
        self.desired_grad_date = desired_grad_date
        self.note = ""
        self.max_credits_per_term = max_credits_per_term

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

    def add_course(self, course_name: str, year: int, term: int):
        """
        Function adds a course to the course object into self.student plan with
        position being determined by inputted "year" and "term"

        Inputs:
            course_name - (str) identifier of the course to add
            year - (int) indicates the year in which to add the course in self.plan
            term - (int) indicats the term in which to add the course in self.plan

        """
        added_course = None

        #get course object that coresponds to the inputted course_name
        for degree in self.degree_list:
            for course in degree.courses:
                if course.name == course_name:
                    added_course = course
                    break
        #add course object into self.plan and courses_taken
        self.plan[year][term].append(added_course)
        self.courses_taken.append(added_course)


    def remove_course(self, course_name: str, year: int, term: int):
        """
        Function removes a course from the course object from self.student plan
        with position being determined by inputted "year" and "term"

        Inputs:
            course_name - (str) identifier of the course to add
            year - (int) indicates the year in which to add the course in self.plan
            term - (int) indicats the term in which to find the course in self.plan

        """

        #check to confirm course is in self.plan
        course_found = False
        for course in self.plan[year][term]:
            if course.name == course_name:
                course_found = True
                self.plan[year][term].remove(course)
                self.courses_taken.remove(course)

        if course_found == False:
            print("Error")

    def get_plan(self):

        #calculate the pre_req_num for the degrees
        for degree in self.degree_list:
            degree.calc_pre_req_nums()

        return generate_plan(self)

    def checkcompetion(self):
        """
        check if all degrees for the student has had their requirements met
        """
        pass
