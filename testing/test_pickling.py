"""
--------------------------------------------------------------------------------
File containing nose tests for pickling.py.

Author: River Veek
Group: TBD
Last Modified: 2/25/21
--------------------------------------------------------------------------------
"""

import nose
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
            else:
                print("File doesn't exist\n")

    @nose.with_setup(teardown)
    def test_save_and_load(self):
        """Test the saving and loading of an object."""
        id = "951234567"
        test_obj = {"test1": 4, "test2": 16}
        save_record(id, test_obj)
        loaded_obj = load_record(id)
        assert loaded_obj["test1"] == 4
