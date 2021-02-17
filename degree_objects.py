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

        #loop through courses in the major
        for course in self.courses:
            #loop through pre_reqs for the currnt course
            for pre_req in course.pre_reqs:
                pre_req.pre_reqs_num += 1

        return None


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
