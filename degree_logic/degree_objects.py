"""
----------------------------------------------------------------------------------------
File for the defining the Degree class object and Course class object

Authors - JT Kashuba, Noah Kruss
Group - TBD
Last Modified - 3/6/21
----------------------------------------------------------------------------------------
"""
from enum import Enum

class Degree():

    # def __init__(self, name: str):
    def __init__(self, name):
        """
        required_courses - (list) is a list of course_num / levels
        """

        self.name = name
        self.courses = []
        self.core_courses = []

    def __repr__(self):
        """
        Function to state what should be printed when a degree object in printed
        """

        return self.name

    def calc_pre_req_nums(self):
        """
        Function that calculates (and sets the integer value for) the number of courses
        that each course in the Degree object relies upon (is a prereq for).

        Returns:
            None
        """
        #ensure everything is zeroed out
        for course in self.courses:
            course.pre_reqs_num = 0

        #loop through courses in the major
        for course in self.courses:
            temp = course.pre_reqs[:]
            while len(temp) != 0:
                #loop through pre-req courses
                for pre_req_course in temp:
                    #increment pre req counter for pre_req_course by 1
                    pre_req_course.pre_reqs_num += 1
                    #add pre_req_course's pre-reqs to the temp list
                    temp += pre_req_course.pre_reqs[:]
                    #remove pre_req_course from temp list
                    temp.remove(pre_req_course)

        return None

    def add_course(self,
                   name,
                   course_num,
                   num_credits,
                   pre_reqs,
                   terms,
                   is_core = False,
                   difficulty = 2):
        """
        Function for creating a new Course object and adding it to the degree

        Note: Course must have all pre-reqs already added to the degree

        Inputs:
            name - (str) is the unique name for the course
            course_num - (int) is the identifier number for the course
            num_credits - (int) is the number of credits the Univerity give the course
            pre_reqs - (list) is a list of course names that are required to
                        be taken by a Student before this one
            terms - (list) is a list of Term objects
            is_core - (bool) a string denoting what type of requirment the
                            core course to complete the major. Defaults to False
            difficulty - (int) is a integer repersenting how difficult the course
                         is on a scale of 1 to 5

        Outputs:
            None
        """

        #get pre_req objects
        pre_req_objects = []
        for course in self.courses:
            if course.name in pre_reqs:
                pre_req_objects.append(course)

        #error check to confirm all pre_req were found in the degree object
        if len(pre_req_objects) != len(pre_reqs):
            print("Error adding ", name, ": could not find all of the pre-reqs in the degree")
            return None

        #generate Course object
        new_course = Course(name, course_num, num_credits, pre_req_objects, terms, difficulty)

        #add Course into list of possible courses
        self.courses.append(new_course)

        if is_core:
            self.core_courses.append(new_course)

    # def remove_course(self, name: str):
    def remove_course(self, name):
        """
        Function to remove a course with course.name == name from degree object

        Inputs:
            name - (str) is the unique name for the course

        Outputs:
            None
        """

        #remove from general list
        for course in self.courses:
            if course.name == name:
                self.courses.remove(course)

        #remove from core list
        for course in self.core_courses:
            if course.name == name:
                self.core_courses.remove(course)

    # def get_course(self, target_course_name: str):
    def get_course(self, target_course_name):
        for course in self.courses:
            if course.name == target_course_name:
                print(course.name)
                return course

    def save_degree(self):
        self.calc_pre_rec_nums()
        pass


class Course():

    # def __init__(self, name: str, course_num: int, num_credits: int, pre_reqs: list, terms: list, difficulty: int):
    def __init__(self, name, course_num, num_credits, pre_reqs, terms, difficulty):
        """
        Function to initialize a Course object

        Inputs:
            name - (str) is the unique name for the course
            course_num - (int) is the identifier number for the course
            num_credits - (int) is the number of credits the Univerity give the course
            pre_reqs - (list) is a list of Course objects that are required to
                        be taken by a Student before this one
            terms - (list) is a list of Term objects
            difficulty - (int) is a integer repersenting how difficult the course
                         is on a scale of 1 to 5
        """
        #Base infomation
        self.name = name
        self.num_credits = num_credits
        self.pre_reqs = pre_reqs
        self.terms = terms
        self.difficulty = difficulty

        #Counter for how many courses require this one to be taken before hand
        self.pre_reqs_num = 0

        #Course difficulty properties
        self.course_num = course_num

    def __repr__(self):
        """
        Function to state what should be printed when a course in printed
        """

        return self.name


class Term():
    """
    object for Term
    """

    # def __init__(self, term_name: str):
    def __init__(self, term_name):

        self.value = 0
        self.name = term_name;

        if term_name == "Fall":
            self.value = 0
        elif term_name == "Winter":
            self.value = 1
        elif term_name == "Spring":
            self.value = 2
        elif term_name == "Summer":
            self.value = 3
