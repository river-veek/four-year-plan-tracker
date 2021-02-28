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
sys.path.append("../degree_logic")

from student_objects import *
from CIS_degree import *
from Gen_Ed import *

CIS_major = create_CIS_major()
GEN_Ed = create_Gen_Ed()

def test_create_student():
    student_A = Student("student_A")
    studnet_A.add_degree(CIS_major)

    student_B = Student("student_B", summer=True)
    studnet_B.add_degree(CIS_major)

    student_C = Student("student_C", desired_grad_date = ("Fifth", 2))
    studnet_C.add_degree(CIS_major)

    student_D = Student("student_D", summer=True, desired_grad_date = ("Fifth", 2))
    studnet_D.add_degree(CIS_major)

def test_add_class():
    pass

def test_change_grad_date():
    pass

def test_change_summer():
    pass

def test_create_plan():
    pass

def main():
    student_A = Student("student_A")
    student_A.add_degree(CIS_major)
    student_A.add_degree(GEN_Ed)
    student_A.add_course("MATH 112 Elementary Functions", 1, 0)
    #student_A.add_course("CIS 443 User Interfaces", 1, 1)
    # student_A.add_course("CIS 322 Introduction to Software Engineering", 1, 1)
    # student_A.add_course("CIS 322 Introduction to Software Engineering", 1, 1)
    forecast_plan = student_A.get_plan()

main()
