"""
--------------------------------------------------------------------------------
File containing nose tests for degree_objects.py.

Author: River Veek
Group: TBD
Last Modified: 3/6/21
--------------------------------------------------------------------------------
"""
import nose
import sys
sys.path.append("./degree_logic")
from degree_objects import *


class Test_degree_object:
    """Tests for degree_objects.py."""

    def test_add_course_not_core(self):
        """Test adding single non-core course to dummy degree object."""
        deg = Degree("TEST")
        term1 = Term("Fall")
        deg.add_course("Non-Core Class", 101, 4, [], [term1])

        assert len(deg.courses) == 1
        assert len(deg.core_courses) == 0
        assert deg.courses[0].name == "Non-Core Class"
        assert deg.courses[0].num_credits == 4
        assert len(deg.courses[0].pre_reqs) == 0
        assert len(deg.courses[0].terms) == 1
        assert deg.courses[0].terms == [term1]
        assert deg.courses[0].course_num == 101

    def test_add_course_is_core(self):
        """Test adding single core course to dummy degree object."""
        deg = Degree("TEST")
        term1 = Term("Fall")
        deg.add_course("Is-Core Class", 101, 4, [], [term1], is_core=True)

        assert len(deg.courses) == 1
        assert len(deg.core_courses) == 1
        assert deg.courses[0].name == "Is-Core Class"
        assert deg.core_courses[0].name == "Is-Core Class"
        assert deg.courses[0].num_credits == 4
        assert len(deg.courses[0].pre_reqs) == 0
        assert len(deg.courses[0].terms) == 1
        assert deg.courses[0].terms == [term1]
        assert deg.courses[0].course_num == 101

    def test_add_course_with_prereqs(self):
        """Test adding single core course (with prerequisites) to dummy degree object."""
        deg = Degree("TEST")
        term1 = Term("Fall")
        deg.add_course("Course 1", 101, 4, [], [term1], is_core=True)
        deg.add_course("Course 2", 102, 4, ["Course 1"], [term1], is_core=True)

        assert len(deg.courses[1].pre_reqs) == 1
        assert deg.courses[1].pre_reqs[0].name == "Course 1"

    def test_remove_course(self):
        """Test removing course (with no prerequisites) from dummy degree object."""
        deg = Degree("TEST")
        term1 = Term("Fall")
        deg.add_course("Course 1", 101, 4, [], [term1], is_core=True)
        deg.remove_course("Course 1")

        assert len(deg.courses) == 0

    def test_remove_course(self):
        """Test removing course that does not exist from dummy degree object."""
        deg = Degree("TEST")
        deg.remove_course("Course 1")

        assert len(deg.courses) == 0

    def test_calc_pre_req_nums(self):
        """Test number of courses that rely on a given course."""
        deg = Degree("TEST")
        term1 = Term("Fall")
        deg.add_course("Course 1", 101, 4, [], [term1], is_core=True)
        deg.add_course("Course 2", 102, 4, ["Course 1"], [term1], is_core=True)
        deg.add_course("Course 3", 103, 4, ["Course 1"], [term1], is_core=True)
        deg.add_course("Course 4", 104, 4, ["Course 2"], [term1], is_core=True)
        deg.add_course("Course 5", 105, 4, ["Course 4"], [term1], is_core=True)
        deg.calc_pre_req_nums()

        assert deg.courses[0].pre_reqs_num == 4
        assert deg.courses[1].pre_reqs_num == 2
        assert deg.courses[2].pre_reqs_num == 0
        assert deg.courses[3].pre_reqs_num == 1
        assert deg.courses[4].pre_reqs_num == 0
