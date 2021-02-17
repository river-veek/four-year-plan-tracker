"""
--------------------------------------------------------------------------------
File for saving and loading pickle objects

Author - Zeke Petersen
Group - TBD
Last Modified - 2/17/21
--------------------------------------------------------------------------------
"""

import pickle

def save_record(student_id, student_object):
    """
    :student_id: Student.identifier string
    :student_object: Student class object to be pickled

    No return value. Creates a new pickle file of the name <student_id>.
    """
    path = './pickles/' + student_id
    pickle_out = open(path, "wb")
    pickle.dump(student_object, pickle_out)
    pickle_out.close()
    return

def load_record(student_id):
    """
    :student_id: Student.identifier string

    Returns a Python object (in this case, a Student) from the file named
    <student_id>.
    """
    path = './pickles/' + student_id
    pickle_in = open(path, "rb")
    student = pickle.load(pickle_in)
    pickle_in.close()
    return student

def testing():
    test_obj = {"test1": 4, "test2": 16}
    save_record("951234567", test_obj)
    loaded_obj = load_record("951234567")
    assert loaded_obj["test1"] == 4

def main():
    print("----------- Begin testing ------------\n")
    testing()
    print("---------- All tests passed ----------\n")


if __name__ == '__main__':
    main()
