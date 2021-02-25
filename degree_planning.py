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
    print_plan(forecast_plan)

    #initialize unmet_courses
    unmet_courses = []
    for degree in student.degree_list:
        unmet_courses += degree.core_courses.copy()

    #set current term
    current_term = ("First", 0)

    #remove courses from unmet_courses if in student plan
    for key in student.plan:
        for term in student.plan[key]:
            #check that the term is not empty
            for course in term:
                #if course is in unmet_courses remove it
                if course in unmet_courses:
                    unmet_courses.remove(course)
                #update current term
                current_term = (key, term)

    #print(f"UNSORTED - {unmet_courses}")
    for course in unmet_courses:
        print(course.name, course.pre_reqs_num)

    #sort this unmet_courses by pre_rec_nums
    unmet_courses.sort(key=sort_pre_req)

    print(f"SORTED - {unmet_courses}")

    ###figure out the number of terms remaining before the desired grad date
    # if student.summer == True:
    #     num_terms_remaining = ((grad_year - current_year) * 4) + (grad_term - start_term)
    # else:
    #     num_terms_remaining = ((grad_year - current_year) * 3) + (grad_term - start_term)
    #
    # ###based off this number determine number of courses that need to be taken per term
    # courses_per_term = len(unmet_courses) % num_terms_remaining
    # print(courses_per_term)

    ###loop through unmet list popping off the from of the list and adding to the plan

    return forecast_plan

def sort_pre_req(course):
    return course.pre_reqs_num

def print_plan(plan):

    print("----------------------------")
    for year in plan:
        string = ""
        for term in plan[year]:
            string += "| "
            for course in term:
                string += course.name
        print(string)
        print("----------------------------")
