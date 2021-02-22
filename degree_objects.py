"""
----------------------------------------------------------------------------------------
File for the defining the Degree class object and Course class object

Author - Noah Kruss
Group - TBD
Last Modified - 2/21/21
----------------------------------------------------------------------------------------
"""

class Degree():

    def __init__(self, name: str):
        """
        required_courses - (list) is a list of course_num / levels
        """

        self.name = name
        self.courses = []
        self.course_requirments = {}

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
                   requirment_type = None):
        """
        Function for creating a new Course object and adding it to the degree

        Note: Course must have all pre-reqs alreay added to the degree

        Inputs:
            name - (str) is the unique name for the course
            course_num - (int) is the identifier number for the course
            pre_reqs - (list) is a list of course names that are required to
                        be taken by a Student before this one
            terms - (list) is a list of Term enums
            requirment_type - (str) a string denoting what type of requirment the
                              course is. Defaults to None

        Outputs:
            None
        """

        #get pre_req objects
        pre_req_objects = []
        for course in self.courses:
            if course.name is in pre_reqs:
                pre_req_objects.append(course)

        if len(pre_req_objects) != len(pre_reqs):
            print("Error loading pre-reqs could not find all of them in the degree")
            return None

        #generate Course object
        new_course = Course(name, course_num, pre_req_objects, terms)

        #add Cource into list of possible cources
        self.courses.append(new_course)

        if requirment_type == None:
            pass
        elif self.required_courses.has_key(requirment_type):
            self.required_courses[requirment_type].append(new_course)
        else:
            self.required_courses[requirment_type] = [new_course]

        #THOUGHTS!!!!!!!!!!!!!!!!!!!
        #recalc pre reqs num
        self.calc_pre_rec_nums()

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

        #remove from required_courses
        for requirment_type in self.required_courses:
            for course in self.core_courses:
                if course.name == name:
                    self.courses.remove(course)

        #THOUGHTS!!!!!!!!!!!!!!!!!!!
        #recalc pre reqs num
        self.calc_pre_rec_nums()

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

        #Base infomation
        self.name = name
        self.pre_reqs = pre_reqs
        self.terms = terms

        #Counter for how many courses require this one to be taken before hand
        self.pre_reqs_num = 0

        #Course difficulty properties
        self.course_num = course_num
        self.level = (course_num % 100) * 100


class Term(Enum):
    """
    object for Term
    """

    "Fall" = 0
    "Winter" = 1
    "Spring" = 2
    "Summer" = 3
