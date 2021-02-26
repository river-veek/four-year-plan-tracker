"""
----------------------------------------------------------------------------------------
File for generating the Gen_Ed object

Author - JT Kashuba
Group - TBD
Last Modified - 2/24/21
----------------------------------------------------------------------------------------
"""

from degree_objects import *

def create_Gen_Ed():
    Gen_Ed = Degree("Gen_Ed")

    # 15 credits of Arts and Letters
    Gen_Ed.add_course("Arts and Letters Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Arts and Letters Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Arts and Letters Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Arts and Letters Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

    # 15 credits of Social Sciences
    Gen_Ed.add_course("Social Science Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Social Science Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Social Science Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Social Science Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

    # Writing 121 and 122
    Gen_Ed.add_course("WR 121 College Composition I", 121, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("WR 122 College Composition II", 121, 4, ["WR 121 College Composition I"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

    # --------------------------------------------------------------------------
    # Question for Noah since he's the architect: How do we handle this case, where
    # a student needs to pick 1 elective from 2 of these 3 options. Unsure how to implement
    # so included all 3 below. Guessing we'll need to only have 2 but not sure where
    # the add_course dropdown button will be populating from.. and it needs to recognize
    # these 3 distinct options
    # --------------------------------------------------------------------------

    # 8 credits for multicultural requirement (must pick from 2 of 3 categories AC, IP, IC)
    #    - AC = American Cultures
    #    - IP = Identity, Pluralism, Tolerance
    #    - IC = International Cultures
    Gen_Ed.add_course("Multicultural Elective (AC)", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Multicultural Elective (IP)", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Multicultural Elective (IC)", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)


    return Gen_Ed
