"""
--------------------------------------------------------------------------------
File containing the routing for application logic

Author: JT Kashuba, Logan Levitre, Zeke Petersen
Group: TBD
Last Modified: 3/5/21
--------------------------------------------------------------------------------
"""

from __future__ import print_function # In python 2.7
from flask import Flask, render_template, abort, request, jsonify, json, redirect, url_for
import random
import sys

sys.path.append('./degree_logic') # Required to find the following degree logic modules
import degree_planning as dp
import pickling as pkl
import CIS_degree as cd
import Gen_Ed as ge
from student_objects import *

app = Flask(__name__)

@app.route("/")
@app.route("/index", methods=['POST'])
def index():
	"""
	Landing page

	Populates dropdowns of the main user interface
	"""
	names = pkl.create_studentID_list()  # Gather the existing student objects
	courses = gen_courses()  # All possible courses from the CIS/GenEd major objects

	# Pass all info pertaining to dropdowns, some are globals
	return render_template('ui.html', names=names, terms=terms, years=years, courses=courses)

# Creating route, including POST method
@app.route("/forecast", methods=['POST'])
def forecast():
	"""
	Forecast page

	Handles a login, save (without displaying), and save (with a forecast display)
	"""
	# using JSON to get data from form - gets string of list - needs to be passed to render_temp
	request_data = request.get_json()

	# Debug statements
	# print(request_data, file=sys.stderr)
	# print(request_data.keys(), file=sys.stderr)

	global student_obj

	# only has one key
	tmp = request_data.keys()

	# Handle which button was called based on the keys in the JSON

	# 'Create' button or ID selected from dropdown
	if tmp[0] == 'login':
		# used for testing data transfer
		# print("LOGIN", file=sys.stderr)
		# print("ID", request_data['login'], file=sys.stderr)

		# Get the student id from the front end
		id = request_data['login']

		# Attempt to load a record, returns None if it isn't in our records
		student_obj = pkl.load_record(str(id))

		# If we don't have a student already (new student was selected), then make a new default object
		if student_obj == None:
			student_obj = Student(id)
			deg = cd.create_CIS_major()
			student_obj.add_degree(deg)
			gen_ed = ge.create_Gen_Ed()
			student_obj.add_degree(gen_ed)
		return "Logged in"

	# Save and Display
	elif tmp[0] == 'tableData':
		# used for testing data transfer
		# print("Clicked Save/Display", file=sys.stderr),
		# print("Saved Classes: ", request_data['tableData'], file=sys.stderr)

		# Add each course in the table
		for i in range(len(request_data['tableData'])):
			year = 1
			term = 1

			# add_course expects ints, convert based on the strings populating the frontend (globals terms and years)
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

		# Generate a forecast
		forecast_dict = student_obj.get_plan()

		# Parse it in a format that HTML/Jinja can easily handle
		forecast_adjusted = format_rows_to_columns(forecast_dict)

		# Save the record after all courses are added
		pkl.save_record(student_obj.identifier, student_obj)

		# Give the forecast to the HTML, one table for each year in the forecast
		return render_template('forecast.html', forecast_rows=forecast_adjusted)

	# Save
	elif tmp[0] == 'savedData':
		# used for testing data transfer
		# print('Clicked Save', file=sys.stderr)
		# print("Saved Classes: ", request_data['savedData'], file=sys.stderr)

		# Add each course in the table
		for i in range(len(request_data['savedData'])):
			year = 1
			term = 1

			# add_course expects ints, convert based on the strings populating the frontend (globals terms and years)
			if request_data['savedData'][i][2] == u'1st':
				year = 1
			elif request_data['savedData'][i][2] == u'2nd':
				year = 2
			elif request_data['savedData'][i][2] == u'3rd':
				year = 3
			elif request_data['savedData'][i][2] == u'4th':
				year = 4
			elif request_data['savedData'][i][2] == u'5th':
				year = 5

			if request_data['savedData'][i][1] == u'Fall':
				term = 0
			elif request_data['savedData'][i][1] == u'Winter':
				term = 1
			elif request_data['savedData'][i][1] == u'Spring':
				term = 2
			elif request_data['savedData'][i][1] == u'Summer':
				term = 3

			student_obj.add_course(request_data['savedData'][i][0], year, term)

		# Save the student record after all courses are added
		pkl.save_record(student_obj.identifier, student_obj)

		return "Saved Successfully"

	# prints to browser console it has been saved
	return "Saved Successfully"

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
		for term_i in range(len(student_plan[year])):
			term = student_plan[year][term_i]
			if term_i == 0:
				fall_col.append(term)
			elif term_i == 1:
				winter_col.append(term)
			elif term_i == 2:
				spring_col.append(term)
			elif term_i == 3:
				summer_col.append(term)

	# formatted_columns is a list containing 5 sub-lists
	# These sub-lists represents the courses taken in the 1st year, 2nd year,
	# and so on. They are formatted to display as columns rather than rows.

	# For example:
	# example = [
	#       [ ["CIS 210", "CIS 211", "CIS 212", ""], ["CIS 110", "CIS 111", "CIS 199", ""] ],
	#       [ ["CIS 313", "CIS 315", "CIS 425", ""], ["CIS 314", "MATH 343", "CIS 471", ""] ]
	#           ]
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
	formatted_columns = []
	for year in student_plan:
		# This is hardcoding the max number of courses taken each term (4 lists
		# of empty strings to be in line with the established 16 credit max set in student_objects)
		formatted_columns.append([ ["", "", "", ""],["", "", "", ""],["", "", "", ""], ["", "", "", ""] ])

	# formatted_columns[i][j][0]
	# i represents which Year the courses were taken
	# j represents how many courses taken that term
	# 0 is hard coding the location for Fall
	fall_col_len = len(fall_col)
	for i in range(fall_col_len):
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

	return formatted_columns

def gen_courses():
	"""
	Helper function to populate the course dropdown. Creates a list of every course
	in every degree necessary for a CIS student.

	Currently static since this app only supports CIS students. Can be changed later
	to create a dropdown list for a different type of student in future development.
	"""
	dummy_student = Student("951234567")
	dummy_gen_ed = ge.create_Gen_Ed()
	dummy_student.add_degree(dummy_gen_ed)
	dummy_deg = cd.create_CIS_major()
	dummy_student.add_degree(dummy_deg)
	return dummy_student.get_course_list()

if __name__ == "__main__":

	# Global objects that the app wants to track or populate for the user
	global student_obj
	global terms
	global years

	# Can add more elements if we wish to extend how many years users can add courses to
	terms = ["Fall", "Winter", "Spring", "Summer"]
	years = ["1st", "2nd", "3rd", "4th", "5th"]
	student_obj = None

	app.run(threaded=False,debug=True,host='0.0.0.0')
