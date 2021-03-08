"""
----------------------------------------------------------------------------------------
File for defining functions for generating a degree plan

Authors - Noah Kruss, River Veek
Group - TBD
Last Modified - 3/7/21
----------------------------------------------------------------------------------------
"""

import sys
sys.path.append("./degree_logic")
from student_objects import *
from degree_objects import *

def create_test_degree():
	test_major = Degree("Test Major")

	################# Writing and Math Pre-Requisites ##########################
	# --------------------------------------------------------------------------
	test_major.add_course("WR 121 College Composition I", 121, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")])
	test_major.add_course("WR 122 College Composition II", 121, 4, ["WR 121 College Composition I"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")])

	# Math 112 added as a pre-req (alternatively this can be satisfied by an adequate placement test score)
	test_major.add_course("MATH 112 Elementary Functions", 112, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

	# Discrete Math I & II (required of CIS majors)
	test_major.add_course("MATH 231 Elements of Discrete Mathematics I", 231, 4, ["MATH 112 Elementary Functions"], [Term("Fall"), Term("Winter"), Term("Spring")], is_core = True)
	test_major.add_course("MATH 232 Elements of Discrete Mathematics II", 232, 4, ["MATH 231 Elements of Discrete Mathematics I"], [Term("Fall"), Term("Winter"), Term("Spring")], is_core = True)
	# --------------------------------------------------------------------------

	##################### 200 level test courses ########################
	# --------------------------------------------------------------------------
	test_major.add_course("CIS 210 Computer Science I", 210, 4, ["MATH 112 Elementary Functions"], [Term("Fall"), Term("Winter")], is_core = True)
	test_major.add_course("CIS 211 Computer Science II", 211, 4, ["CIS 210 Computer Science I"], [Term("Winter"), Term("Spring")], is_core = True)
	test_major.add_course("CIS 212 Computer Science III", 212, 4, ["CIS 211 Computer Science II"], [Term("Fall"), Term("Spring")], is_core = True)
	# --------------------------------------------------------------------------

	######################## 300 level CIS courses #############################
	# --------------------------------------------------------------------------
	test_major.add_course("CIS 313 Intermediate Data Structures", 313, 4, ["CIS 212 Computer Science III", "MATH 232 Elements of Discrete Mathematics II"], [Term("Fall"), Term("Winter")], is_core = True)
	test_major.add_course("CIS 314 Computer Organization", 314, 4, ["CIS 212 Computer Science III", "MATH 231 Elements of Discrete Mathematics I"], [Term("Winter"), Term("Spring")], is_core = True)
	test_major.add_course("CIS 315 Intermediate Algorithms", 315, 4, ["CIS 313 Intermediate Data Structures"], [Term("Winter"), Term("Spring")], is_core = True)
	test_major.add_course("CIS 322 Introduction to Software Engineering", 322, 4, ["CIS 212 Computer Science III"], [Term("Fall"), Term("Spring")])
	test_major.add_course("CIS 330 C/C++ & Unix", 330, 4, ["CIS 314 Computer Organization"], [Term("Winter"), Term("Spring")], is_core = True)
	# --------------------------------------------------------------------------

	################# Upper Division (400 level) CIS courses ###################
	# --------------------------------------------------------------------------
	test_major.add_course("CIS 415 Operating Systems", 415, 4, ["CIS 313 Intermediate Data Structures", "CIS 330 C/C++ & Unix"], [Term("Fall"), Term("Spring")], is_core = True)
	test_major.add_course("CIS 429 Computer Architecture", 431, 4, ["CIS 330 C/C++ & Unix"], [Term("Spring")])
	# --------------------------------------------------------------------------

	################# CIS Electives (400/300 level) ###################
	# --------------------------------------------------------------------------
	test_major.add_course("CIS Elective 400+", 400, 4, ["CIS 212 Computer Science III"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
	test_major.add_course("CIS Elective 300+", 300, 4, ["CIS 212 Computer Science III"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
	# --------------------------------------------------------------------------

	################# MATH Electives (300 level) ###################
	# --------------------------------------------------------------------------
	test_major.add_course("MATH Elective 300+", 300, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
	# --------------------------------------------------------------------------

	return test_major

class Test_degree_planning:
	"""Tests for degree_planning.py."""

	def test_generate_plan(self):
		"""Verify that all required courses (from dummy degree object) end up in generated plan."""
		test_deg = create_test_degree()
		student = Student("Firstname Lastname")
		student.add_degree(test_deg)
		# student.add_degree(GEN_Ed)
		forecasted_plan = student.get_plan()

		for course in test_deg.core_courses:
			cur_check = False
			for key in forecasted_plan:
				for group in forecasted_plan[key]:
					if course in group:
						cur_check = True
			assert cur_check

	def test_added_courses_generate_plan(self):
		"""
		Verify that all required courses (from dummy degree object) and extra course
		end up in generated plan.
		"""
		test_deg = create_test_degree()
		student = Student("Firstname Lastname")
		test_deg.add_course("Non-Core Class", 101, 4, [], [Term("Fall")])
		student.add_degree(test_deg)
		student.add_course("Non-Core Class", 1, 0)
		forecasted_plan = student.get_plan()
		cur_check = False

		for key in forecasted_plan:
			for group in forecasted_plan[key]:
				for course in group:
					if course.name == "Non-Core Class":
						cur_check = True
		assert cur_check

	def test_added_300_upper_division_generate_plan(self):
		"""
		Verify that added 300-level upper division course replaces generic CIS 300-level upper division
		elective from generated plan.
		"""
		test_deg = create_test_degree()
		student = Student("Firstname Lastname")
		# test_deg.add_course("Non-Core Class", 101, 4, [], [Term("Fall")])
		student.add_degree(test_deg)
		student.add_course("CIS 322 Introduction to Software Engineering", 1, 0)
		forecasted_plan = student.get_plan()
		cur_check = True

		for key in forecasted_plan:
			for group in forecasted_plan[key]:
				for course in group:
					if course.name == "CIS Elective 300+":
						cur_check = False
		assert cur_check

	def test_added_400_upper_division_generate_plan(self):
		"""
		Verify that added 400-level upper division course replaces generic CIS 400-level upper division
		elective from generated plan.
		"""
		test_deg = create_test_degree()
		student = Student("Firstname Lastname")
		# test_deg.add_course("Non-Core Class", 101, 4, [], [Term("Fall")])
		student.add_degree(test_deg)
		student.add_course("CIS 429 Computer Architecture", 1, 0)
		forecasted_plan = student.get_plan()
		cur_check = True
		check_300_exists = False

		for key in forecasted_plan:
			for group in forecasted_plan[key]:
				for course in group:
					if course.name == "CIS Elective 400+":
						cur_check = False
					if course.name == "CIS Elective 300+":
						check_300_exists = True
		assert cur_check and check_300_exists

from Gen_Ed import *
from CIS_degree import *
GEN_Ed = create_Gen_Ed()
CIS_major = create_CIS_major()
def main():
	student_A = Student("student_A")
	student_A.add_degree(CIS_major)
	student_A.add_degree(GEN_Ed)
	#student_A.add_course("CIS 110 Fluency with Information Technology", 1, 1)
	student_A.add_course("WR 121 College Composition I", 1, 0)
	#student_A.add_course("Arts and Letters Elective", 1, 1)

	# student_A.add_course("CIS 322 Introduction to Software Engineering", 1, 1)
	# student_A.add_course("CIS 322 Introduction to Software Engineering", 1, 1)
	forecast_plan = student_A.get_plan()

main()
