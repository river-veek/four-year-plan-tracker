"""
--------------------------------------------------------------------------------
File containing the routing for application logic

Author: JT Kashuba, Logan Levitre, Zeke Petersen
Group: TBD
Last Modified: 3/3/21
--------------------------------------------------------------------------------
"""
from __future__ import print_function # In python 2.7
from flask import Flask, render_template, abort, request, jsonify, json, redirect, url_for
import random
import sys

# import degree_planning as dp
# import pickling as pkl
# import CIS_degree as cd
# import Gen_Ed as ge
# from student_objects import *


app = Flask(__name__)

# Dummy info for passing to html
names = ["951234567", "951234568", "951234569"]
terms = ["Fall", "Winter", "Spring", "Summer"]
years = ["1st", "2nd", "3rd", "4th", "5th"]
courses = ["CIS 210", "CIS 211", "CIS 212"]

# dummy_student = Student("951234567")
# dummy_gen_ed = ge.create_Gen_Ed()
# dummy_student.add_degree(dummy_gen_ed)
# dummy_deg = cd.create_CIS_major()
# dummy_student.add_degree(dummy_deg)
# courses = dummy_student.get_course_list()

# Starting with this class arrangement (by row instead of year) just to make it easier
# to make sure django code in the HTML is working (we can parse the python to match this if absolutely necessary)
forecast_rows = [
                [["CIS 210", "CIS 211", "CIS 212", ""],["CIS 110", "CIS 111", "CIS 199", ""]],
                [["CIS 313", "CIS 315", "CIS 425", ""],["CIS 314", "MATH 343", "CIS 471", ""]]
                ]

student_obj = None

@app.route("/")
@app.route("/index", methods=['POST'])
def index():
    """
    Landing page
    """

    """ Psuedocode

	# terms and years can be static globals since those should be the same no matter what
	names = pkl.create_studentID_list()

	# TODO -- create this function, for our program this will need to be static since we have not yet loaded the student_obj
	courses = generate_course_list()  # All possible courses from the CIS/GenEd major objects (not sure if this exists yet)

	"""
    return render_template('ui.html', names=names, terms=terms, years=years, courses=courses)

# Going off JT's project creating route, including GET/POST methods
@app.route("/forecast", methods=['POST'])
def forecast():
	"""
	Forecast page

	"""
	# using JSON to get data from form - gets string of list - needs to be passed to render_temp

	request_data = request.get_json()
	print(request_data, file=sys.stderr)
	print(request_data.keys(), file=sys.stderr)

	# only has one key
	tmp = request_data.keys()
	# will need to use to designate what button was called tableData - Save and display
	# savedData - Save button - will need global variable to contain all saved data and add each time most likely?
	if tmp[0] == 'login':
		print("LOGIN", file=sys.stderr)
		print("ID", request_data['login'], file=sys.stderr)

		""" Pseudocode

		id = request_data['login']
		student_obj = pkl.load_record(id)

		if student_obj == None:
			student_obj = Student(id)
			gen_ed = ge.create_Gen_Ed()
			student_obj.add_degree(gen_ed)
			deg = cd.create_CIS_major()
			student_obj.add_degree(deg)

			# TODO -- any other prep for this new object?

		"""

	if tmp[0] == 'tableData':
		# used for testing data transfer
		print("Clicked Save/Display", file=sys.stderr),
		print("Saved Classes: ", request_data['tableData'], file=sys.stderr)

		""" Pseudocode

		# TODO -- is this the proper way to call add_course?
		for i in range(len(request_data['tableData'])):
			year = 1
			term = 1
			if request_data['tableData'][i][2] == u'1st':
				year = 1
			elif request_data['tableData'][i][2] == u'2nd':
				year = 2
			elif request_data['tableData'][i][2] == u'3rd':
				year = 3
			elif request_data['tableData'][i][2] == u'4th':
				year = 4
			elif request_data['tableData'][i][2] == u'5th':
				year = 5

			if request_data['tableData'][i][1] == u'Fall':
				term = 0
			elif request_data['tableData'][i][1] == u'Winter':
				term = 1
			elif request_data['tableData'][i][1] == u'Spring':
				term = 2
			elif request_data['tableData'][i][1] == u'Summer':
				term = 3

			student_obj.add_course(request_data['tableData'][i][0], year, term)

		# TODO -- is this the proper way to get the plan?
		# forecast = dp.generate_plan(student_obj)
		forecast_dict = student_obj.get_plan()
		forecast_adjusted = format_rows_to_columns(forecast_dict)

		pkl.save_record(student_obj.identifier, student_obj)

		return render_template('forecast.html', forecast_rows=forecast_adjusted)
		"""

		result = get_data(request_data)
		return render_template('forecast.html', forecast_rows=result)

	elif tmp[0] == 'savedData':
		print('Clicked Save', file=sys.stderr)
		print("Saved Classes: ", request_data['savedData'], file=sys.stderr)

		""" Pseudocode

		# TODO -- is this the proper way to call add_course?
		for i in range(len(request_data['tableData'])):
			year = 1
			term = 1

			if request_data['tableData'][i][2] == u'1st':
				year = 1
			elif request_data['tableData'][i][2] == u'2nd':
				year = 2
			elif request_data['tableData'][i][2] == u'3rd':
				year = 3
			elif request_data['tableData'][i][2] == u'4th':
				year = 4
			elif request_data['tableData'][i][2] == u'5th':
				year = 5

			if request_data['tableData'][i][1] == u'Fall':
				term = 0
			elif request_data['tableData'][i][1] == u'Winter':
				term = 1
			elif request_data['tableData'][i][1] == u'Spring':
				term = 2
			elif request_data['tableData'][i][1] == u'Summer':
				term = 3

			student_obj.add_course(request_data['tableData'][i][0], year, term)

		pkl.save_record(student_obj.identifier, student_obj)

		return "Saved Successfully"
		"""
	#prints to browser console it has been saved
	return "Saved Successfully"

def get_data(data):
	# print("IN GET DATA", data, file=sys.stderr)
	# print(len(data), file=sys.stderr)
	# needs to be formatted to correct list format for forecasting page
	arr = (data['tableData'])
	print(arr, file=sys.stderr)
	return arr

def format_rows_to_columns(forecast_dict):
    """
    Helper function to reformat list of courses from Student object's
    self.plan (student_object.py) into a format appropriate for forecast.html
    i.e. rows from student object will be converted into columns for forecast.html
    """
    # these lists will contain the info for the columns but will still need
    # to be parsed as columns later. for now, they are lists of lists, where the
    # inner lists represent different years. i.e. fall_col will have the form:
    # fall_col = [ [year 1 fall courses], [year 2 fall courses], etc]
    fall_col = []
    winter_col = []
    spring_col = []
    summer_col = []
    student_plan = forecast_dict
    # grabs the inner lists from the dictionary that represent each term from
    # their corresponding year (the key represents the year, the value represents
    # the courses taken that year, with it's inner lists being each term in that year)
    # stores all the lists of the Fall term courses from each year in "fall_col",
    # each year's Winter terms in winter_col, and so on.
    for year in student_plan:
        for term in student_plan[year]:
            if term == student_plan[year][0]:
                fall_col.append(term)
            elif term == student_plan[year][1]:
                winter_col.append(term)
            elif term == student_plan[year][2]:
                spring_col.append(term)
            elif term == student_plan[year][3]:
                summer_col.append(term)

    # formatted_columns is a list containing 5 sub-lists
    # These sub-lists represents the courses taken in the 1st year, 2nd year,
    # and so on. They are formatted to display as columns rather than rows.

    # For example:
    # example = [
    #       [["CIS 210", "CIS 211", "CIS 212", ""],["CIS 110", "CIS 111", "CIS 199", ""]],
    #       [["CIS 313", "CIS 315", "CIS 425", ""],["CIS 314", "MATH 343", "CIS 471", ""]]
    #                 ]
    # This example list represents a possible course-plan for the 1st and 2nd year,
    # where Year 1 Fall Term the student is taking CIS 210 and CIS 110
    # Year 1 Winter Term the student is taking CIS 211 and CIS 111
    # Year 1 Spring Term the student is taking CIS 212 and CIS 199
    # Year 1 Summer Term the student is taking no courses

    # Year 2 Fall Term the student is taking CIS 313 and CIS 314
    # Year 2 Winter Term the student is taking CIS 315 and MATH 343
    # Year 2 Spring Term the student is taking CIS 425 and CIS 471
    # Year 2 Summer Term the student is taking no courses

    # Assumes a maximum of 4 courses allowed per term
    formatted_columns = [ [ [],[],[],[] ],
                          [ [],[],[],[] ],
                          [ [],[],[],[] ],
                          [ [],[],[],[] ],
                          [ [],[],[],[] ],
                          ]
    # formatted_columns[i][j][0]
    # i represents which Year the courses were taken
    # j represents how many courses taken that term
    # 0 is hard coding the location for Fall
    fall_col_len = len(fall_col)
    for i in range(fall_col_len)):
        fall_col_i_len = len(fall_col[i])
        for j in range(fall_col_i_len):
            formatted_columns[i][j][0] = fall_col[i][j].name

    # formatted_columns[i][j][1]
    # i represents which Year the courses were taken
    # j represents how many courses taken that term
    # 1 is hard coding the location for Winter
    winter_col_len = len(winter_col)
    for i in range(winter_col_len):
        winter_col_i_len = len(winter_col[i])
        for j in range(winter_col_i_len):
            formatted_columns[i][j][1] = winter_col[i][j].name

    # formatted_columns[i][j][2]
    # i represents which Year the courses were taken
    # j represents how many courses taken that term
    # 2 is hard coding the location for Spring
    spring_col_len = len(spring_col)
    for i in range(spring_col_len):
        spring_col_i_len = len(spring_col[i])
        for j in range(spring_col_i_len):
            formatted_columns[i][j][2] = spring_col[i][j].name

    # formatted_columns[i][j][3]
    # i represents which Year the courses were taken
    # j represents how many courses taken that term
    # 3 is hard coding the location for Summer
    summer_col_len = len(summer_col)
    for i in range(summer_col_len):
        summer_col_i_len = len(summer_col[i])
        for j in range(summer_col_i_len):
            formatted_columns[i][j][3] = summer_col[i][j].name

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
