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
    # These have been commented out of the Gen_Ed object in order to properly use WR 122 as the pre-req for WR 320/321 in the CIS_degree object
    # This will need to be handled if/when the system is taken to further iterations that handle multiple different degree paths.
    #Gen_Ed.add_course("WR 121 College Composition I", 121, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    #Gen_Ed.add_course("WR 122 College Composition II", 121, 4, ["WR 121 College Composition I"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)

    # --------------------------------------------------------------------------
    # TODO: How do we handle this case, where a student needs to pick 1 elective
    # from 2 of these 3 options. Unsure how to implement so included all 3 below.
    # Now commented out.
    # Eventually it needs to recognize these 3 distinct options, but for now it's
    # been handled by making them generic electives
    # --------------------------------------------------------------------------

    # 8 credits for multicultural requirement (must pick from 2 of 3 categories AC, IP, IC)
    #    - AC = American Cultures
    #    - IP = Identity, Pluralism, Tolerance
    #    - IC = International Cultures
    #Gen_Ed.add_course("Multicultural Elective (AC)", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    #Gen_Ed.add_course("Multicultural Elective (IP)", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    #Gen_Ed.add_course("Multicultural Elective (IC)", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Multicultural Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    Gen_Ed.add_course("Multicultural Elective", 100, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)


    return Gen_Ed
