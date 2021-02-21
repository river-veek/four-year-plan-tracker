"""
----------------------------------------------------------------------------------------


Author - Noah Kruss
Group - TBD
Last Modified - 2/16/21
----------------------------------------------------------------------------------------
"""

class Degree():
    #need to determine how to handle requirements such as X number of 400 level

    def __init__(self, name: str):
        """
        required_courses - (list) is a list of course_num / levels
        """

        self.name = name
        self.courses = []
        self.core_courses = []
        self.required_electives = []

    def calc_pre_rec_nums(self):
        """
        Function to calculate and set the number of courses each courses within
        the Degree are required for (Course.pre_reqs_num)

        Returns:
            None
        """
        #insure everything is zeroed out
        for course in self.courses:
            course.pre_reqs_num = 0

        #loop through courses in the major
        for course in self.courses:
            #loop through pre_reqs for the currnt course
            for pre_req in course.pre_reqs:
                pre_req.pre_reqs_num += 1

        return None

    def add_course(self,
                   name: str,
                   course_num: int,
                   pre_reqs: list,
                   terms: list,
                   is_core_course: bool,
                   is_elective: bool):
        """
        Function for creating a new Course object and adding it to the degree

        Inputs:
            name - (str) is the unique name for the course
            course_num - (int) is the identifier number for the course
            pre_reqs - (list) is a list of Course objects that are required to
                        be taken by a Student before this one
            terms - (list) is a list of Term enums

        Outputs:
            None
        """
        #generate Course object
        new_course = Course(name, course_num, pre_reqs, terms)

        #add Cource into list of possible cources
        self.courses.append(new_course)

        #if core requirment add it to the list
        if is_core_course:
            self.core_courses.append(new_course)

        if is_elective:
            self.required_electives.append(new_course)

    def remove_course(self, name: str):
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
                self.courses.remove(course)

        #remove from elective list
        for course in self.required_electives:
            if course.name == name:
                self.courses.remove(course)

    def save_degree(self):
        pass


class Course():

    def __init__(self, name: str, course_num: int, pre_reqs: list, terms: list):
        """
        Function to initialize a Course object

        Inputs:
            name - (str) is the unique name for the course
            course_num - (int) is the identifier number for the course
            pre_reqs - (list) is a list of Course objects that are required to
                        be taken by a Student before this one
            terms - (list) is a list of Term enums

        """

        self.name = name
        self.pre_reqs = pre_reqs
        self.terms = terms

        self.pre_reqs_num = 0

        self.course_num = course_num
        self.level = (course_num % 100) * 100


class Term(Enum):
    """
    object for Term
    """

    Fall = 0
    Winter = 1
    Spring = 2
    Summer = 3
