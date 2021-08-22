"""
Author(s): River Veek, Noah Kruss

Date: 29 July 2021
"""

from mysql.connector import *

##DONT THINK THIS IS NEEDED
#--------------------CREATE THE DATABASE---------------------------------
#create database function: gotten from the following webpage
    #(https://dev.mysql.com/doc/connector-python/en/connector-python-example-ddl.html)
# def create_database(cursor):
#     try:
#         cursor.execute(
#             "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(DB_NAME))
#     except mysql.connector.Error as err:
#         print("Failed creating database: {}".format(err))
#         exit(1)
#
# cnx = mysql.connector.connect(user='Creator')
# cursor = cnx.cursor()
#
# #try to connect to database
# try:
#     cursor.execute("USE {}".format(DB_NAME))
# #if database does not exist call create_database() to make it
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_BAD_DB_ERROR:
#         create_database(cursor)
#         cnx.database = DB_NAME
#     else:
#         exit(1)

#--------------------CREATE THE DATABASE STRUCTURE------------------------------
def create_DB_tables():
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    #--------------------DEFINE DATABASE TABLES (and Name)----------------------
    DB_NAME = "4YP_DataBase"
    TABLES = {}

    # Users table
    TABLES['Users'] = (

        "CREATE TABLE `Users` ("
        "   `User_ID` INT(9) NOT NULL AUTO_INCREMENT,"
        "   `Username` VARCHAR(50) NOT NULL,"
        "   `Password` VARCHAR(50) NOT NULL,"
        "   `Auth_Level` INT(1) DEFAULT 0"
        "   `Max_Credits` INT(2) DEFAULT 16"
        "   `Summer_Courses` INT(1) DEFAULT 0"
        "   PRIMARY KEY(`User_ID`)"
        "   UNIQUE(`User_ID`, `Username`)"
        ")"

    )

    # Degrees table
    TABLES['Degrees'] = (

        "CREATE TABLE `Degrees` ("
        "   `Degree_ID` INT(4) NOT NULL AUTO_INCREMENT,"
        "   `Degree_Name` VARCHAR(100) NOT NULL,"
        "   `Req_300_Credits` INT(2) NOT NULL DEFAULT 0,"
        "   `Req_400_Credits` INT(2) NOT NULL DEFAULT 0,"
        "   PRIMARY KEY(`Degree_ID`),"
        "   UNIQUE(`Degree_ID`, `Degree Name`)"
        ")"
    )

    # Pursued_Degrees table
    TABLES['Pursued_Degrees'] = (

        "CREATE TABLE `Pursued_Degrees` ("
        "   `Pursued_ID` INT(7) NOT NULL AUTO_INCREMENT,"
        "   `User_ID_FK` INT(9) NOT NULL,"
        "   `Degree_ID_FK` INT(4) NOT NULL,"
        "   PRIMARY KEY(`Pursued_ID`),"
        "   UNIQUE(`Pursued_ID`)"
        "   FOREIGN KEY (`User_ID_FK`) "
        "       REFERENCES Users(`User_ID`)"
        "       ON DELETE CASCADE,"
        "   FOREIGN KEY (`Degree_ID_FK`) "
        "       REFERENCES Degrees(`Degree_ID`)"
        "       ON DELETE CASCADE"
        ")"
    )

    # Courses table
    TABLES['Courses'] = (

        "CREATE TABLE `Courses` ("
        "   `Course_ID` INT(7) NOT NULL AUTO_INCREMENT,"
        "   `Course_Name` VARCHAR(50) NOT NULL,"
        "   `Course_Number` INT(8) NOT NULL,"
        "   `Has_Prereqs` INT(1) NOT NULL DEFAULT 0,"
        "   `Difficulty_Level` INT(2) NOT NULL DEFAULT 5,"
        "   `Terms` INT(2) NOT NULL DEFAULT 0,"
        "   `Num_Credits` INT(2) NOT NULL DEFAULT 4,"
        "   PRIMARY KEY(`Course_ID`),"
        "   UNIQUE(`Course_ID`, `Course_Name`)"
        ")"
    )

    # Prereqs table
    TABLES['Prereqs'] = (

        "CREATE TABLE `Prereqs` ("
        "   `Prereq_ID` INT(7) NOT NULL AUTO_INCREMENT,"
        "   `Course_ID_FK` NOT NULL,"
        "   `Course_ID_Dependent_FK` NOT NULL,"
        "   PRIMARY KEY(`Prereq_ID`),"
        "   UNIQUE(`Prereq_ID`)"
        "   FOREIGN KEY (`Course_ID_FK`) "
        "       REFERENCES Courses(`Course_ID`)"
        "       ON DELETE CASCADE,"
        "   FOREIGN KEY (`Course_ID_Dependent_FK`) "
        "       REFERENCES Courses(`Course_ID`)"
        "       ON DELETE CASCADE"
        ")"

    )

    # Courses_Taken table
    TABLES['Courses_Taken'] = (

        "CREATE TABLE `Courses_Taken` ("
        "   `Taken_ID` INT(9) NOT NULL AUTO_INCREMENT,"
        "   `User_ID_FK` INT(9) NOT NULL,"
        "   `Course_ID_FK` INT(7) NOT NULL,"
        "   `Term_Taken` INT(2) NOT NULL,"
        "   PRIMARY KEY(`Taken_ID`),"
        "   UNIQUE(`Taken_ID`)"
        "   FOREIGN KEY (`User_ID_FK`) "
        "       REFERENCES Users(`User_ID`)"
        "       ON DELETE CASCADE,"
        "   FOREIGN KEY (`Course_ID_FK`) "
        "       REFERENCES Courses(`Course_ID`)"
        "       ON DELETE CASCADE"
        ")"

    )

    #initilize the tables that will comprise the database
    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("already exists.")
            else:
                print(err.msg)
        else:
            print("OK")

    cursor.close()
    cnx.close()

#need to create function for making table creating statement and row adding statement for new degree table
def create_degree_table(degree_name):
    #create table design
    table_description = (

        f"CREATE TABLE {degree_name} ("
        "   `Core_ID` INT(3) NOT NULL AUTO_INCREMENT,"
        "   `Course_ID_FK` INT(7) NOT NULL,"
        "   PRIMARY KEY(`Core_ID`),"
        "   UNIQUE(`Core_ID`),"
        "   FOREIGN KEY (`Course_ID_FK`) "
        "       REFERENCES Courses(`Course_ID`)"
        "       ON DELETE CASCADE"
        ")"
    )

    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    try:
        cursor.execute(table_description)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print("already exists.")
        else:
            print(err.msg)

    cursor.close()
    cnx.close()

#--------------------STATEMENTS FOR ADDING NEW ROWS TO THE TABLES
    #modled off of https://dev.mysql.com/doc/connector-python/en/connector-python-example-cursor-transaction.html

add_Course_Taken = ("INSERT INTO Courses_Taken "
               "(Taken_ID, User_ID_FK, Course_ID_FK, Term_Taken) "
               "VALUES (%s, %s, %s, %s)")

#need to add functionality to encript the user password (should use a hash)
def add_user(User_ID, Username, Password, Auth_Level, Max_Credits, Summer_Courses):
    """
    Function for accessing the system database and updating a new row of data to
    the User table

    Inputs:
        User_ID - (int) Unique number identifier connected with the user
        Username - (str) String identifier for user
        Password - (str)
        Auth_Level - (int) int value (0, 1, or 2) to identify the users level
                     of authorization for the system
                         0 -> Student User
	                     1 -> Advisor User
	                     2 -> Administration User
        Max_Credits - (int)
        Summer_Courses - (int) intiger value of 0 or 1 repersenting whether or
                         not the user is willing to take summer courses
                            0 -> No, not willing to take summer courses
	                        1 -> Yes, willing to take summer course

    Returns:
        None
    """
    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    new_user = (User_ID, Username, Password, Auth_Level, Max_Credits, Summer_Courses)

    add_user_statement  = ("INSERT INTO Users "
                           "(User_ID, Username, Password, Auth_Level, Max_Credits, Summer_Courses) "
                           "VALUES (%s, %s, %s, %s, %s)")

    cursor.execute(add_user_statement, new_user)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

def add_degree(Degree_ID, Degree_Name, Req_300_Credits, Req_400_Credits):
    """
    Function for accessing the system database and updating a new row of data to
    the Degree table

    Inputs:
        Degree_ID - (int) Unique number identifier connected with the degree
        Degree_Name - (str) Unique string identifier for Degree
        Req_300_Credits - (int) int values representing how many 300+ level credits
                           are needed for the degree
        Req_400_Credits - (int) int values representing how many 400+ level credits
                           are needed for the degree

    Returns:
        None
    """

    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    new_degree = (Degree_ID, Degree_Name, Req_300_Credits, Req_400_Credits)

    add_degree_statement = ("INSERT INTO Degrees "
                            "(Degree_ID, Degree_Name, Req_300_Credits, Req_400_Credits) "
                            "VALUES (%s, %s, %s, %s)")

    cursor.execute(add_degree_statement, new_degree)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

def add_pursued_degree(Pursued_ID, User_ID_FK, Degree_ID_FK):
    """
    Function for accessing the system database and updating a new row of data to
    the Pursued Degree table

    Inputs:
        Pursued_ID - (int) Unique number identifier connected with the pursued degree
        User_ID_FK - (int) Foreign key into the Users table to the student
                     pursuing the degree
        Degree_ID_FK - (int) Foreign key into the Degree table of the degree the
                        student is pursuing

    Returns:
        None
    """

    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    new_pursued_degree = (Pursued_ID, User_ID_FK, Degree_ID_FK)

    add_pursued_degree_statement = ("INSERT INTO Pursued_Degrees "
                                    "(Pursued_ID, User_ID_FK, Degree_ID_FK) "
                                    "VALUES (%s, %s, %s)")

    cursor.execute(add_pursued_degree_statement, new_pursued_degree)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

def add_course(Course_ID, Course_Name, Course_Number, Has_Prereqs, Difficulty_Level, Terms, Num_Credits):
    """
    Function for accessing the system database and updating a new row of data to
    the Course table

    Inputs:
        Course_ID  - (int) Unique number identifier connected with the course
        Course_Name - (str) String identifier for the course
        Course_Number - (int) The Course number assigned to the course by the university
        Has_Prereqs - (int) A boolean indicator of whether or not the course
                      possesses any courses that must be taken before it. If the
                      Prereq column stores a 1 then the system will need to refer to
                      the Prerequisite table to trace all of the course requirements.
        Difficulty_Level - (int) Value on a scale of 1-5 of how difficult the
                           course is considered to be
        Terms - (int) 4 digit binary number repersenting what terms the course is
                offered during.
                      1  -   1    -   1    -   1
                    Fall - Winter - Spring - Summer
        Num_Credits - (int) Value of the number of credits the course is

    Returns:
        None
    """

    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    new_course = (Course_ID, Course_Name, Course_Number, Has_Prereqs, Difficulty_Level, Terms, Num_Credits)

    add_course_statement = ("INSERT INTO Courses "
                            "(Course_ID, Course_Name, Course_Number, Has_Prereqs, Difficulty_Level, Terms, Num_Credits) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    cursor.execute(add_course_statement, new_course)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

def add_prereq(Prereq_ID, Course_ID_FK, Course_ID_Dependent_FK):
    """
    Function for accessing the system database and updating a new row of data to
    the Prereq table

    Inputs:
        Prereq_ID - (int) Unique number identifier connected with the prereq
        Course_ID_FK - (int) Foreign key into the Course table to course that IS
                        the prereq
        Course_ID_Dependent_FK - (int) Foreign key into the Course table to course
                                that the prereq is dependent on

    Returns:
        None
    """

    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    new_prereq = (Prereq_ID, Course_ID_FK, Course_ID_Dependent_FK)

    add_prereq_statement = ("INSERT INTO Prereqs "
                   "(Prereq_ID, Course_ID_FK, Course_ID_Dependent_FK) "
                   "VALUES (%s, %s, %s)")

    cursor.execute(add_prereq_statement, new_prereq)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()

def add_course_taken(Taken_ID, User_ID_FK, Course_ID_FK, Term_Taken) :
    """
    Function for accessing the system database and updating a new row of data to
    the Pursued Degree table

    Inputs:
        Taken_ID - (int) Unique number identifier connected with the prereq
        User_ID_FK - (int) Foreign key into the Users table to the student
                     taking the course
        Course_ID_FK - (int) Foreign key into the Course table to course that is
                        being taken by the student
        Term_Taken - (str) a string in the form (year, term). For example “10”
                     represents freshman year fall term, “33” represents junior
                     year summer term.

    Returns:
        None
    """

    #connect to the DB
    cnx = mysql.connector.connect(user='FYPT_admin', password='330_PTSD_', database='test-database-1')
    cursor = cnx.cursor()

    new_course_take = (Taken_ID, User_ID_FK, Course_ID_FK, Term_Taken)

    add_course_taken_statement = ("INSERT INTO Courses_Taken "
                                  "(Taken_ID, User_ID_FK, Course_ID_FK, Term_Taken) "
                                "VALUES (%s, %s, %s, %s)")

    cursor.execute(add_course_take_statement, new_course_take)

    # Make sure data is committed to the database
    cnx.commit()
    cursor.close()
    cnx.close()
