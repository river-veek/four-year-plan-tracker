"""
----------------------------------------------------------------------------------------
File for generating the standard CIS degree

Author - Noah Kruss, JT, River
Group - TBD
Last Modified - 2/20/21
----------------------------------------------------------------------------------------
"""
from degree_objects import *

def create_CIS_major():
    #Short Example
    CIS_major = Degree()
    CIS_major.add_course("CIS_110", 110, [], [Term("Fall")])
    CIS_major.add_course("CIS_210", 210, [], [Term("Fall"), Term("Winter")])
    CIS_major.add_course("CIS_211", 211, ["CIS_210"], [Term("Winter"), Term("Spring")])
