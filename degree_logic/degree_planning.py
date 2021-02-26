"""
----------------------------------------------------------------------------------------
File for defining functions for generating a degree plan

Authors - Noah Kruss
Group - TBD
Last Modified - 2/24/21
----------------------------------------------------------------------------------------
"""

def generate_plan(student: "Student"):
    """
    Function for generating a forecast degree plan for a student to meet all
    requirments of their degrees

    Inputs:
        student - Student object of the student to generate the plan for

    Returns:
        forecast_plan
    """

    #create copy of self.plan
    forecast_plan = student.plan.copy()

    #initialize unmet_courses
    unmet_courses = []
    for degree in student.degree_list:
        unmet_courses += degree.core_courses.copy()

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
                #update current term
                current_term = (year, student.plan[year].index(term) + 1)

    #sort this unmet_courses by pre_rec_nums
    unmet_courses.sort(key=sort_pre_req)
    unmet_courses.reverse()

    for course in unmet_courses:
        print(course, course.pre_reqs_num)

    #add courses to forecast_plan
    add_courses_to_forecast(forecast_plan, unmet_courses, current_term, student.summer, student.max_credits_per_term)

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
        plan - degree plan dictonary to print

    Returns:
        None
    """

    print("----------------------------")
    for year in plan:
        string = ""
        for term in plan[year]:
            string += "| ### "
            for course in term:
                string += course.name
                string += " ### "
        print(string)
        print("----------------------------")

def add_courses_to_forecast(plan, unmet_courses: list, current_term: tuple, summer: bool, max_credits_per_term: int):
    """
    Function adding the courses from unmet_courses into the forecast_plan

    Inputs:
        plan - degree plan to be adding courses to
        unmet_courses - list of course objects that need to be added to the plan
        current_term - tuple of the term the student is entering (year, term)
        summer - boolian indicator of whether or not the student is willing to
                 take summer courses
        max_credits_per_term - integer value of how many credits can be taken in
                               a single term

    Returns:
        None
    """

    #find initial term
    current_year = current_term[0]
    current_term = current_term[1]

    #set cap for term
    if summer:
        term_cap = 3
    else:
        term_cap = 2

    #loop until unmet_courses is empty
    while(unmet_courses):
        # get next course and remove it from unmet_courses
        next_course = unmet_courses[0]
        unmet_courses.remove(next_course)

        #find num credits taken in current term
        num_credits = 0
        for course in plan[current_year][current_term]:
            num_credits += course.num_credits

        #check if adding new courses to term will pass max_credits_per_term
        if (num_credits + next_course.num_credits) > max_credits_per_term:
            current_term += 1

            #check if number is past term_cap
            if current_term > term_cap:
                current_term = 0
                current_year = increment_year(plan, current_year)

        #add courses to term
        plan[current_year][current_term].append(next_course)

def increment_year(plan, year: int):
    """
    Function incrementing the year key being used to index through a degree plan.
    If incremented key is out of range of the keys within the degree plan then
    a new year gets added to the degree plan

    Inputs:
        plan - degree plan dictonary to print
        year - year key for the dictonary

    Returns:
        None
    """
    #increment year
    year += 1

    #if year is now not a key in the plan add a new year to the plan
    if year not in plan.keys():
        plan[year] = [[], [], [], []]

    return year
