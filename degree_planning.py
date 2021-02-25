"""
----------------------------------------------------------------------------------------
File for defining functions for generating a degree plan

Authors - Noah Kruss
Group - TBD
Last Modified - 2/24/21
----------------------------------------------------------------------------------------
"""

def generate_plan(student: "Student"):

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

    # print(f"UNSORTED - {unmet_courses}")
    # for course in unmet_courses:
    #     print(course.name, course.pre_reqs_num)

    #sort this unmet_courses by pre_rec_nums
    unmet_courses.sort(key=sort_pre_req)
    unmet_courses.reverse()

    # print(f"SORTED - {unmet_courses}")
    # for course in unmet_courses:
    #     print(course.name, course.pre_reqs_num)

    #add courses to forecast_plan
    add_courses_to_forecast(forecast_plan, unmet_courses, current_term, student.summer, student.max_credits_per_term)

    print_plan(forecast_plan)
    return forecast_plan

#-------------------------------------------------------------------------------
#    Helper Functions
#-------------------------------------------------------------------------------

def sort_pre_req(course):
    return course.pre_reqs_num

def print_plan(plan):

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

def increment_year(plan, year: str):
    year += 1

    #if year is now not a key in the plan add a new year to the plan
    if year not in plan.keys():
        plan[year] = [[], [], [], []]

    return year

def add_courses_to_forecast(plan, unmet_courses: list, current_term: tuple, summer: bool, max_credits_per_term: int):

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
