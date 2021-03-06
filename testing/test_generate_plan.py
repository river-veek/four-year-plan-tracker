"""
----------------------------------------------------------------------------------------
File for defining functions for generating a degree plan

Authors - Noah Kruss
Group - TBD
Last Modified - 2/24/21
----------------------------------------------------------------------------------------
"""

import numpy as np
import sys
sys.path.append("./degree_logic")

from student_objects import *
from CIS_degree import *
from Gen_Ed import *

CIS_major = create_CIS_major()
GEN_Ed = create_Gen_Ed()

def test_create_student():
	student_A = Student("student_A")
	student_A.add_degree(CIS_major)

	student_B = Student("student_B", summer=True)
	student_B.add_degree(CIS_major)

	student_C = Student("student_C", desired_grad_date = ("Fifth", 2))
	student_C.add_degree(CIS_major)

	student_D = Student("student_D", summer=True, desired_grad_date = ("Fifth", 2))
	student_D.add_degree(CIS_major)

def test_add_class():
	pass

def test_change_grad_date():
	pass

def test_change_summer():
	pass

def test_create_plan():
	pass

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

	################# Upper Division (400 level) CIS courses ###################
	# --------------------------------------------------------------------------
	test_major.add_course("CIS 415 Operating Systems", 415, 4, ["CIS 313 Intermediate Data Structures", "CIS 330 C/C++ & Unix"], [Term("Fall"), Term("Spring")], is_core = True)
	test_major.add_course("CIS 429 Computer Architecture", 431, 4, ["CIS 330 C/C++ & Unix"], [Term("Spring")])

	################# CIS Electives (400/300 level) ###################
	# --------------------------------------------------------------------------
	test_major.add_course("CIS Elective 400+", 400, 4, ["CIS 212 Computer Science III"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
	test_major.add_course("CIS Elective 300+", 300, 4, ["CIS 212 Computer Science III"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

	################# MATH Electives (300 level) ###################
	# --------------------------------------------------------------------------
	test_major.add_course("MATH Elective 300+", 300, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

	return test_major

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
