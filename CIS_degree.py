"""
----------------------------------------------------------------------------------------
File for generating the standard CIS degree

Author - Noah Kruss, JT Kashuba, River Veek
Group - TBD
Last Modified - 2/22/21
----------------------------------------------------------------------------------------
"""
from degree_objects import *

def create_CIS_major():
    # Short Example
    CIS_major = Degree()
    CIS_major.add_course("CIS 110 Fluency with Information Technology", 110, [], [Term("Fall")])
    CIS_major.add_course("CIS 210 Computer Science I", 210, ["MATH 112 Elementary Functions"], [Term("Fall"), Term("Winter")])
    CIS_major.add_course("CIS 211 Computer Science II", 211, ["CIS 210 Computer Science I"], [Term("Winter"), Term("Spring")])
    CIS_major.add_course("CIS 212 Computer Science III ", 212, ["CIS 211 Computer Science II"], [Term("Fall"), Term("Spring")])
    CIS_major.add_course("CIS 313 Intermediate Data Structures", 313, ["CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II"], [Term("Fall"), Term("Winter")])
    CIS_major.add_course("CIS 314 Computer Organization", 314, ["CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", "MATH 231 Elements of Discrete Mathematics I"], [Term("Winter"), Term("Spring")])
    CIS_major.add_course("CIS 315 Intermediate Algorithms", 315, ["CIS 313 Intermediate Data Structures"], [Term("Winter"), Term("Spring")])
    CIS_major.add_course("CIS 322 Introduction to Software Engineering", 322, ["CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III"], [Term("Fall"), Term("Spring")])
    CIS_major.add_course("CIS 330 C/C++ & Unix", 330, ["CIS 314 Computer Organization"], [Term("Winter"), Term("Spring")])
    CIS_major.add_course("CIS 399 Applied Cryptography", 399, ["CIS 212 Computer Science III"], [Term("Winter")])
    CIS_major.add_course("CIS 415 Operating Systems", 415, ["CIS 313 Intermediate Data Structures", "CIS 330 C/C++ & Unix"], [[Term("Fall"), Term("Spring")])
    CIS_major.add_course("CIS 425 Principles of Programming Languages", 425, ["CIS 315 Intermediate Algorithms"], [[Term("Fall"), Term("Spring")])
    CIS_major.add_course("CIS 407 Seminar on CIS Careers and Internships", 407, [], [Term("Fall"), Term("Winter"), Term("Spring")])
    CIS_major.add_course("CIS 407 Programming Competition", 407, ["CIS 313 Intermediate Data Structures"], [Term("Fall"), Term("Spring")])
    CIS_major.add_course("CIS 407 Research Colloquia", 407, [], [Term("Fall"), Term("Winter"), Term("Spring")])
    CIS_major.add_course("CIS 410 Computational Science", 410, ["CIS 314 Computer Organization", "CIS 422 Software Methodology"], [Term("Fall")])
    CIS_major.add_course("CIS 410 Computer and Network Security II", 410, [], [Term("Spring")])
    CIS_major.add_course("CIS 410 Computer Vision", 410, [], [Term("Spring")])
    CIS_major.add_course("CIS 410 Internet Measurements", 410, [], [Term("Winter")])
    CIS_major.add_course("CIS 410 Introduction to Game Programming", 410, [], [Term("Spring")])
    CIS_major.add_course("CIS 410 Multi-agent Systems", 410, [], [Term("Spring")])
    CIS_major.add_course("CIS 410 Natural Language Processing", 410, [], [Term("Winter")])
    CIS_major.add_course("CIS 410 Program Analysis and Transformation", 410, [], [Term("Spring")])
    CIS_major.add_course("CIS 410 Secure Software Development", 410, [], [Term("Spring")])
    CIS_major.add_course("CIS 410 Selected Topics on Optimization", 410, [], [Term("Fall")])
