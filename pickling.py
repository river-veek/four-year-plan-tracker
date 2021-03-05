"""
--------------------------------------------------------------------------------
File for saving and loading pickle objects

Author - Zeke Petersen, River Veek
Group - TBD
Last Modified - 3/5/21
--------------------------------------------------------------------------------
"""

import pickle
import os

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
    if not os.path.exists(path):
        return None
    pickle_in = open(path, "rb")
    student = pickle.load(pickle_in)
    pickle_in.close()
    return student

def delete_record(student_id):
    """
    :student_id: Student.identifier string

    No return value. Deletes the file named <student_id> if it exists.
    """
    path = './pickles/' + student_id
    if os.path.exists(path):
        os.remove(path)
    else:
        print("File doesn't exist\n")
    return

def create_studentID_list():
    """Returns a list of all pickle file names (as strings) in pickles/ directory."""
    dir = './pickles/'
    studentID_list = []
    for file in os.listdir(dir):
        path = dir + file
        if os.path.exists(path):
            if not path == "./pickles/tmp.txt" and not path == "./pickles/.DS_Store":  # temp file to make pickles/ a nonempty directory
                studentID_list.append(file)
    return studentID_list

if __name__ == '__main__':
    pass
    # main()
