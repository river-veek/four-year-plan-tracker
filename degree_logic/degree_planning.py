"""
----------------------------------------------------------------------------------------
File for defining functions for generating a degree plan

Authors - Noah Kruss
Group - TBD
Last Modified - 3/3/21
----------------------------------------------------------------------------------------
"""
import copy

# def generate_plan(student: "Student"):
def generate_plan(student):
    """
    Function for generating a forecast degree plan for a student to meet all
    requirements of their degrees

    Inputs:
        student - Student object of the student to generate the plan for

    Returns:
        forecast_plan - dictionary of plan infomation in the following form

            {1: [[course_1, course_2, ...], [course_3, course_4, ...], [], []],
             2: [[], [], [], []],
             3: [[], [], [], []],
             4: [[], [], [], []],
             ...
            }

                Notes: course objects are stored within the lists

                        key:value pairs represent year:courses_taken_that_year,
                        where the inner lists represent each term within that year.
                        The ordering is Fall, Winter, Spring, Summer.
    """

    #create copy of self.plan
    forecast_plan = copy.deepcopy(student.plan)

    #initialize unmet_courses
    unmet_courses = []
    for degree in student.degree_list:
        degree_core_list_copy = degree.core_courses[:]

        #check for repeat courses between degrees
        for course in degree_core_list_copy:
            if course in unmet_courses:
                degree_core_list_copy.remove(course)

        unmet_courses += degree_core_list_copy

    #set current term
    current_term = (1, 0)

    #remove courses from unmet_courses if in student plan
    for year in student.plan:
        for term in student.plan[year]:
            #check that the term is not empty
            for course in term:
                #if course is in unmet_courses remove it
                if course in unmet_courses:
                    unmet_courses.remove(course)
                #elective condition
                else:
                    #loop through the core_courses in degree
                    for core_course in unmet_courses:
                        core_course_degree_name = core_course.name.split()[0]
                        elective_str = core_course.name.split()[1]
                        course_degree_name = course.name.split()[0]

                        #if core_course is an elective
                        if elective_str == "Elective":
                            #if cources are the same major and level requirement it hit
                            if (course_degree_name == core_course_degree_name) and \
                               (course.course_num >= core_course.course_num):

                               unmet_courses.remove(core_course)
                               break

                #update current term
                current_term = (year, student.plan[year].index(term) + 1)

    #sort this unmet_courses by pre_rec_nums
    unmet_courses.sort(key=sort_pre_req)
    unmet_courses.reverse()

    for course in unmet_courses:
        print(course, course.pre_reqs_num)

    #add courses to forecast_plan
    add_courses_to_forecast(forecast_plan, unmet_courses, current_term, student)

    print_plan(student.plan)
    print_plan(forecast_plan)
    return forecast_plan

#-------------------------------------------------------------------------------
#    Helper Functions
#-------------------------------------------------------------------------------

def sort_pre_req(course):
    """
    Function for specifing the paremeter to sort a course list by. This function
    give a sort key of course.pre_reqs_num

    Inputs:
        course - Course object

    Returns:
        course.pre_reqs_num
    """
    return course.pre_reqs_num

def print_plan(plan):
    """
    Function for printing a degree plan to the terminal (Used for progress
    testing)

    Inputs:
        plan - degree plan dictionary to be printed. plan has the following form

            {1: [[course_1, course_2, ...], [course_3, course_4, ...], [], []],
             2: [[], [], [], []],
             3: [[], [], [], []],
             4: [[], [], [], []],
             ...
            }
                Notes: course objects are stored within the lists

                        key:value pairs represent year:courses_taken_that_year,
                        where the inner lists represent each term within that year.
                        The ordering is Fall, Winter, Spring, Summer.

    Returns:
        None
    """
    print("Student Degree Plan")
    print("----------------------------")
    for year in plan:
        string = ""
        for term in plan[year]:
            # string += f"- "
            string += "- "
            for course in term:
                string += course.name
                string += " ### "
            string += "\n"
        # print(string, end=" ")
        print(string)
        print("----------------------------")

# def add_courses_to_forecast(plan, unmet_courses: list, current_term: tuple, student: "Student"):
def add_courses_to_forecast(plan, unmet_courses, current_term, student):
    """
    Function adding the courses from unmet_courses into the forecast_plan

    Inputs:
        plan - degree plan to be adding courses to. plan has the following form
            {1: [[course_1, course_2, ...], [course_3, course_4, ...], [], []],
             2: [[], [], [], []],
             3: [[], [], [], []],
             4: [[], [], [], []],
             ...
            }
                Notes: course objects are stored within the lists

                        key:value pairs represent year:courses_taken_that_year,
                        where the inner lists represent each term within that year.
                        The ordering is Fall, Winter, Spring, Summer.

        unmet_courses - list of course objects that need to be added to the plan
        current_term - tuple of the term the student is entering (year, term)
        student - Student object forecast is being preformed for

    Returns:
        None
    """

    #find initial term
    current_year = current_term[0]
    current_term = current_term[1]

    #set cap for term
    if student.summer:
        term_cap = 3
    else:
        term_cap = 2

    forecasted_courses_taken = student.courses_taken[:]
    current_term_buffer = []

    #check that if the current_term is summer it is allowed
    if (current_term == 3) and (student.summer == False):
        current_term = 0
        current_year = increment_year(plan, current_year)

    #loop until unmet_courses is empty
    while(unmet_courses):

        # get next course and remove it from unmet_courses
        next_course = get_next_course(forecasted_courses_taken, unmet_courses, current_term)
        # print()
        # print(plan)
        # print(next_course)
        # print(current_term)

        if next_course == None:
            #increment term
            current_term += 1

            #add buffered courses into forecasted_courses_taken
            forecasted_courses_taken += current_term_buffer[:]
            #reset current_term_buffer
            current_term_buffer = []

            #check if number is past term_cap
            if current_term > term_cap:
                current_term = 0
                current_year = increment_year(plan, current_year)
        else:
            #find num credits taken in current term
            num_credits = 0
            for course in plan[current_year][current_term]:
                num_credits += course.num_credits

            #check if adding new courses to term will pass max_credits_per_term
            if (num_credits + next_course.num_credits) > student.max_credits_per_term:
                #increment term
                current_term += 1

                #add buffered courses into forecasted_courses_taken
                forecasted_courses_taken += current_term_buffer[:]
                #reset current_term_buffer
                current_term_buffer = []

                #check if number is past term_cap
                if current_term > term_cap:
                    current_term = 0
                    current_year = increment_year(plan, current_year)

            else:
                unmet_courses.remove(next_course)
                unmet_courses.sort(key=sort_pre_req)
                unmet_courses.reverse()
                #add courses to term
                plan[current_year][current_term].append(next_course)

                #add course to current_term_buffer
                current_term_buffer.append(next_course)

def get_next_course(forecasted_courses_taken, unmet_course_list, current_term):
    """
    Function for determining what course should be added to a student plan next

    Inputs:
        forecasted_courses_taken - list of Course objects that are currently in
                                   the students plan for previous terms
        unmet_course_list - list of Course objects that still need to be taken
                            by the student
        current_term - (int) value repersenting the term next_couse is going to
                       be taken in
                            0 = Fall
                            1 = Winter
                            2 = Spring
                            3 = Summer
    Returns:
        next_course - Course object of the next course that should be taken
    """

    incr = 0
    done = False
    while(done == False):
        done = True

        #condition where no course can be found for current term
        if incr >= len(unmet_course_list):
            return None

        next_course = unmet_course_list[incr]
        #check that all pre-reqs have been taken
        for course in next_course.pre_reqs:
            if course not in forecasted_courses_taken:
                done = False

        #check that next_course is offered in current term
        term_valid = False
        for term in next_course.terms:
            if term.value == current_term:
                term_valid = True
        if (term_valid == False):
            done = False

        incr += 1

    return next_course

# def increment_year(plan, year: int):
def increment_year(plan, year):
    """
    Function incrementing the year key being used to index through a degree plan.
    If incremented key is out of range of the keys within the degree plan then
    a new year gets added to the degree plan

    Inputs:
        plan - degree plan dictionary. plan has the following form

            {1: [[course_1, course_2, ...], [course_3, course_4, ...], [], []],
             2: [[], [], [], []],
             3: [[], [], [], []],
             4: [[], [], [], []],
             ...
            }
                Notes: course objects are stored within the lists

                        key:value pairs represent year:courses_taken_that_year,
                        where the inner lists represent each term within that year.
                        The ordering is Fall, Winter, Spring, Summer.

        year - year key (int) for the dictionary

    Returns:
        None
    """
    #increment year
    year += 1

    #if year is now not a key in the plan add a new year to the plan
    if year not in plan.keys():
        plan[year] = [[], [], [], []]

    return year
