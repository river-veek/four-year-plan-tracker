"""
----------------------------------------------------------------------------------------
File for defining Student class object and a class for storing a list of students

Authors - JT Kashuba, Noah Kruss
Group - TBD
Last Modified - 2/22/21
----------------------------------------------------------------------------------------
"""
import degree_objects as d_o
import degree_planning as d_p

class Student():
    """
    Class object to store a student's infomation such a desired graduation date,
    if they are willing to take classes over the summer, and what courses they
    completed
    """
    # def __init__(self,
    #              identifier: str,
    #              summer = False,
    #              desired_grad_date = (4, 2),
    #              max_credits_per_term = 12
    #              ):

    def __init__(self,
                 identifier,
                 summer = False,
                 desired_grad_date = (4, 2),
                 max_credits_per_term = 16
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

    # def add_degree(self, degree_obj: Degree):
    def add_degree(self, degree_obj):
        """
        Function for adding a degree from the student.degree_list

        Inputs:
            degree_obj - (Degree) the Degree object to be added

        Returns:
            None
        """

        self.degree_list.append(degree_obj)

    # def remove_degree(self, degree_name: str):
    def remove_degree(self, degree_name):
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

    # def add_course(self, course_name: str, year: int, term: int):
    def add_course(self, course_name, year, term):
        """
        Function adds a course to the course object into self.student plan with
        position being determined by inputted "year" and "term"

        Inputs:
            course_name - (str) identifier of the course to add
            year - (int) indicates the year in which to add the course in self.plan
                        1 = 1st year
                        2 = 2nd year
                        ...
            term - (int) indicats the term in which to find the course in self.plan
                        0 = Fall
                        1 = Winter
                        2 = Spring
                        3 = Summer
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

    # def remove_course(self, course_name: str, year: int, term: int):
    def remove_course(self, course_name, year, term):
        """
        Function removes a course from the course object from self.student plan
        with position being determined by inputted "year" and "term"

        Inputs:
            course_name - (str) identifier of the course to add
            year - (int) indicates the year in which to add the course in self.plan
                        1 = 1st year
                        2 = 2nd year
                        ...
            term - (int) indicats the term in which to find the course in self.plan
                        0 = Fall
                        1 = Winter
                        2 = Spring
                        3 = Summer

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
        """
        Function to generate a possible plan for the student to complete all of
        the requirments for the degrees they are taking

        Returns:
            plan - dictonary of plan infomation in the following form

                {1: [[course_1, course_2, ...], [course_3, course_4, ...], [], []],
                 2: [[], [], [], []],
                 3: [[], [], [], []],
                 4: [[], [], [], []],
                 ...
                }

                    Note - course objects are stored within the lists
        """

        #calculate the pre_req_num for the degrees
        for degree in self.degree_list:
            degree.calc_pre_req_nums()

        return d_p.generate_plan(self)

    def get_course_list(self):
        """
        Function to return a list of the string names of all course objects that
        are within the degrees within self.degree_list

        Returns:
            course_list - list of course names
        """

        #initilize list
        course_list =[]

        #loop through degrees
        for degree in self.degree_list:
            #loop through courses within the degree
            for course in degree.courses:
                #check that the course isn't already in the list
                if course.name not in course_list:
                    #add course
                    course_list.append(course.name)

        return course_list
