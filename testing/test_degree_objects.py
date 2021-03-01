"""
--------------------------------------------------------------------------------
File containing nose tests for degree_objects.py.

Author: River Veek
Group: TBD
Last Modified: 2/28/21
--------------------------------------------------------------------------------
"""
import nose
import sys
sys.path.append("../degree_logic")
from degree_objects import *


class Test_degree_object:

    def test_add_course(self):
        """Test adding single course to dummy degree object."""
        deg = Degree("TEST")
        term1 = Term("Fall")
        deg.add_course("Course 1", 101, 4, [], [term1])
        assert len(deg.courses) == 1
        assert deg.courses[0].name == "Course 1"
        assert deg.courses[0].num_credits == 4
        assert len(deg.courses[0].pre_reqs) == 0
        assert len(deg.courses[0].terms) == 1
        assert deg.courses[0].terms == [term1]
        assert deg.courses[0].course_num == 101
