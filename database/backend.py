"""
Author(s): River Veek, Noah Kruss

Date: 29 July 2021
"""

from mysql.connector import *

TABLES = {}

# TODO: Double check correctness of 'foreign key' constraint where necessary

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

#example Specific degree table
TABLES['CIS_Major'] = (

    "CREATE TABLE `CIS_Major` ("
    "   `Core_ID` INT(3) NOT NULL AUTO_INCREMENT,"
    "   `Course_ID_FK` INT(7) NOT NULL,"
    "   PRIMARY KEY(`Core_ID`),"
    "   UNIQUE(`Core_ID`),"
    "   FOREIGN KEY (`Course_ID_FK`) "
    "       REFERENCES Courses(`Course_ID`)"
    "       ON DELETE CASCADE"
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
    "   `Has_Prereqs` INT(1) NOT NULL DEFAULT 0,"
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
