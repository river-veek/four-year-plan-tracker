"""
--------------------------------------------------------------------------------
File containing nose tests for pickling.py.

Author: River Veek
Group: TBD
Last Modified: 2/25/21
--------------------------------------------------------------------------------
"""

import nose
import sys
# sys.path.append("../")
from pickling import *

class TestPickling:
    """Tests for pickling files."""

    def teardown(self):
        """Removes all pickle objects created from running tests."""
        dir = './pickles/'
        for file in os.listdir(dir):
            path = dir + file
            if os.path.exists(path):
                if not path == "./pickles/tmp.txt":
                    os.remove(path)
                    pass
            else:
                print("File doesn't exist\n")

    @nose.with_setup(teardown)
    def test_create_studentID_list(self):
        """Check that all pickle files are being added to a list."""
        studentID_list = ["951234567", "952468910", "959595959"]
        id1 = "951234567"
        test_obj = {"test1": 4, "test2": 16}
        save_record(id1, test_obj)
        id2 = "952468910"
        test_obj = {"test1": 4, "test2": 16}
        save_record(id2, test_obj)
        id3 = "959595959"
        test_obj = {"test1": 4, "test2": 16}
        save_record(id3, test_obj)
        assert sorted(create_studentID_list()) == sorted(studentID_list)

    @nose.with_setup(teardown)
    def test_save_and_load(self):
        """Test the saving and loading of an object."""
        id = "951234567"
        test_obj = {"test1": 4, "test2": 16}
        save_record(id, test_obj)
        loaded_obj = load_record(id)
        assert loaded_obj["test1"] == 4
