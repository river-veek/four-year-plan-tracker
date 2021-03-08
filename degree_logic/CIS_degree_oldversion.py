#---------------previous instantiation of cis degree object---------------------
# This CIS_major degree object took all previous pre-requisites into account before
# the back-end logic was implemented to only need the most recent pre-requisite
# associated with each course.

# It is saved here and commented out if there is ever a use for the hard-coded
# robust version of the CIS_major degree object.


    # CIS_major = Degree("CIS Major")
    #
    # ################# Writing and Math Pre-Requisites ##########################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("WR 121 College Composition I", 121, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")])
    # CIS_major.add_course("WR 122 College Composition II", 121, 4, ["WR 121 College Composition I"], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")])
    #
    # # TODO: MATH 101 + 112 are not explicitly required if the student has an adequate placement test score - this needs handling
    # CIS_major.add_course("MATH 101 Foundations of Algebra and Mathematical Modeling", 101, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # # Math 112 added as a pre-req (alternatively this can be satisfied by an adequate placement test score)
    # CIS_major.add_course("MATH 112 Elementary Functions", 112, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    #
    # # Discrete Math I & II (required of CIS majors)
    # CIS_major.add_course("MATH 231 Elements of Discrete Mathematics I", 231, 4, ["MATH 112 Elementary Functions"], [Term("Fall"), Term("Winter"), Term("Spring")], is_core = True)
    # CIS_major.add_course("MATH 232 Elements of Discrete Mathematics II", 232, 4, ["MATH 112 Elementary Functions", "MATH 231 Elements of Discrete Mathematics I"], [Term("Fall"), Term("Winter"), Term("Spring")], is_core = True)
    # # --------------------------------------------------------------------------
    #
    #
    # ##################### 100 and 200 level CIS courses ########################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("CIS 110 Fluency with Information Technology", 110, 4, [], [Term("Fall"), Term("Summer")])
    # CIS_major.add_course("CIS 111 Introduction to Web Programming", 111, 4, ["MATH 101 Foundations of Algebra and Mathematical Modeling"], [Term("Winter"), Term("Summer")])
    # CIS_major.add_course("CIS 122 Intro to Programming and Problem Solving", 122, 4, ["MATH 101 Foundations of Algebra and Mathematical Modeling"], [Term("Fall"), Term("Spring"), Term("Summer")])
    # # TODO: are there multiple CIS 199 offerings? on summer 2020 CIS 199
    # # is labeled "Sp St Managing Soc Med"
    # CIS_major.add_course("CIS 199 Fundamentals of Computer and Information Security", 199, 4, [], [Term("Fall"), Term("Summer")])
    # CIS_major.add_course("CIS 210 Computer Science I", 210, 4, ["MATH 112 Elementary Functions"], [Term("Fall"), Term("Winter")], is_core = True)
    # CIS_major.add_course("CIS 211 Computer Science II", 211, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I"], [Term("Winter"), Term("Spring")], is_core = True)
    # CIS_major.add_course("CIS 212 Computer Science III", 212, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II"], [Term("Fall"), Term("Spring")], is_core = True)
    # # --------------------------------------------------------------------------
    #
    #
    # ######################## 300 level CIS courses #############################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("CIS 313 Intermediate Data Structures", 313, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II"], [Term("Fall"), Term("Winter")], is_core = True)
    #
    # CIS_major.add_course("CIS 314 Computer Organization", 314, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I"], [Term("Winter"), Term("Spring")], is_core = True)
    #
    # CIS_major.add_course("CIS 315 Intermediate Algorithms", 315, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures"], \
    #                             [Term("Winter"), Term("Spring")], is_core = True)
    #
    # CIS_major.add_course("CIS 322 Introduction to Software Engineering", 322, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III"], \
    #                         [Term("Fall"), Term("Spring")])
    #
    # CIS_major.add_course("CIS 330 C/C++ & Unix", 330, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "CIS 314 Computer Organization"], [Term("Winter"), Term("Spring")], is_core = True)
    #
    # # TODO: there are multiple CIS 399 offerings, but there is no definitive list
    # # there were 2 offered in 2020 summer "Sp St Android Apps" and "Sp St iOS Apps Dev"
    # # and I know there is also 399 Data Science
    # CIS_major.add_course("CIS 399 Applied Cryptography", 399, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III"], \
    #                         [Term("Winter"), Term("Summer")])
    # # --------------------------------------------------------------------------
    #
    #
    # ########################## 407 seminars ####################################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("CIS 407 Seminar on CIS Careers and Internships", 407, 2, [], [Term("Fall"), Term("Winter"), Term("Spring")])
    # CIS_major.add_course("CIS 407 Seminar on Principles of Programming Languages", 407, 2, [], [Term("Spring")])
    # CIS_major.add_course("CIS 407 Programming Competition", 407, 2, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures"], [Term("Fall"), Term("Spring")])
    # CIS_major.add_course("CIS 407 Research Colloquia", 407, 2, [], [Term("Fall"), Term("Winter"), Term("Spring")])
    # # --------------------------------------------------------------------------
    #
    #
    # # TODO: there is a CIS 409 "Prac Supv Consulting" that was offered summer 2020 but doesn't show up on the
    # # CIS 2020/2021 courses page, as is the case of the previous TODO comments
    #
    #
    # ################# Upper Division (400 level) CIS courses ###################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("CIS 415 Operating Systems", 415, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", \
    #                         "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix"], [Term("Fall"), Term("Spring")], is_core = True)
    #
    # CIS_major.add_course("CIS 425 Principles of Programming Languages", 425, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 315 Intermediate Algorithms"], \
    #                         [Term("Fall"), Term("Spring")], is_core = True)
    #
    # CIS_major.add_course("CIS 413 Advanced Data Structures", 413, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 315 Intermediate Algorithms"], \
    #                         [Term("Winter")])
    #
    # CIS_major.add_course("CIS 420 Automata Theory", 420, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 315 Intermediate Algorithms"], \
    #                         [Term("Fall")])
    #
    # CIS_major.add_course("CIS 422 Software Methodology", 422, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures"], \
    #                         [Term("Fall"), Term("Winter"), Term("Spring")], is_core = True)
    #
    # CIS_major.add_course("CIS 429 Computer Architecture", 431, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix"], [Term("Spring")])
    #
    # CIS_major.add_course("CIS 431 Introduction to Parallel Computing", 431, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix"], [Term("Winter")])
    #
    # # TODO: 432 *recommends* taking CIS 415 but doesn't require it, how to handle?
    # CIS_major.add_course("CIS 432 Intro to Computer Networks", 432, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix"], [Term("Fall")])
    #
    # CIS_major.add_course("CIS 433 Computer & Network Security", 433, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", \
    #                         "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix", "CIS 415 Operating Systems"], [Term("Winter")])
    #
    # CIS_major.add_course("CIS 441 Intro Computer Graphics", 441, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix"], [Term("Spring")])
    #
    # CIS_major.add_course("CIS 443 User Interfaces", 443, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures"], [Term("Fall")])
    #
    # CIS_major.add_course("CIS 445 Modeling and Simulation", 445, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 314 Computer Organization", "CIS 315 Intermediate Algorithms", \
    #                         "CIS 330 C/C++ & Unix"], [Term("Spring")])
    #
    # CIS_major.add_course("CIS 451 Database Processing", 451, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 314 Computer Organization"], \
    #                         [Term("Fall")])
    #
    # CIS_major.add_course("CIS 471 Introduction to Artificial Intelligence", 471, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 315 Intermediate Algorithms"], \
    #                         [Term("Fall"), Term("Winter")])
    #
    # CIS_major.add_course("CIS 472 Machine Learning", 472, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 315 Intermediate Algorithms"], \
    #                         [Term("Fall"), Term("Spring")])
    #
    # CIS_major.add_course("CIS 473 Probabilistic Methods", 473, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 315 Intermediate Algorithms"], \
    #                         [Term("Winter")])
    # # --------------------------------------------------------------------------
    #
    #
    # ######################### 410 offerings ####################################
    # # --------------------------------------------------------------------------
    # # TODO: CIS 410 Computational Science pre-reqs can be waived w/ Instructor's consent, how to handle?
    # CIS_major.add_course("CIS 410 Computational Science", 410, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "MATH 231 Elements of Discrete Mathematics I", "MATH 232 Elements of Discrete Mathematics II", "CIS 313 Intermediate Data Structures", "CIS 314 Computer Organization", \
    #                         "CIS 422 Software Methodology"], [Term("Fall")])
    #
    # CIS_major.add_course("CIS 410 Computer and Network Security II", 410, 4, [], [Term("Spring")])
    # CIS_major.add_course("CIS 410 Computer Vision", 410, 4, [], [Term("Spring")])
    # CIS_major.add_course("CIS 410 Internet Measurements", 410, 4, [], [Term("Winter")])
    # CIS_major.add_course("CIS 410 Introduction to Game Programming", 410, 4, [], [Term("Spring")])
    # CIS_major.add_course("CIS 410 Multi-agent Systems", 410, 4, [], [Term("Spring")])
    # CIS_major.add_course("CIS 410 Natural Language Processing", 410, 4, [], [Term("Winter")])
    # CIS_major.add_course("CIS 410 Program Analysis and Transformation", 410, 4, [], [Term("Spring")])
    #
    # CIS_major.add_course("CIS 410 Secure Software Development", 410, 4, ["MATH 112 Elementary Functions", "CIS 210 Computer Science I", "CIS 211 Computer Science II", "CIS 212 Computer Science III", \
    #                         "CIS 322 Introduction to Software Engineering", "MATH 231 Elements of Discrete Mathematics I", "CIS 314 Computer Organization", "CIS 330 C/C++ & Unix", \
    #                         "CIS 399 Applied Cryptography"], [Term("Spring")])
    #
    # CIS_major.add_course("CIS 410 Selected Topics on Optimization", 410, 4, [], [Term("Fall")])
    # # --------------------------------------------------------------------------
    #
    #
    # ######################### Writing elective #################################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("Writing 320/321", 320, 4, ["WR 121 College Composition I", "WR 122 College Composition II"], [Term("Fall"), Term("Winter"), Term("Spring")], is_core = True)
    # # --------------------------------------------------------------------------
    #
    #
    # ################ Upper Division Math electives #############################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("MATH Elective 300+", 300, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # CIS_major.add_course("MATH Elective 300+", 300, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # # --------------------------------------------------------------------------
    #
    #
    # ################ 3-course Science sequence electives #######################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("SCIENCE Elective 200+", 200, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # CIS_major.add_course("SCIENCE Elective 200+", 200, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # CIS_major.add_course("SCIENCE Elective 200+", 200, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # # --------------------------------------------------------------------------
    #
    #
    # ################## Upper Division CIS electives ############################
    # # --------------------------------------------------------------------------
    # CIS_major.add_course("CIS Elective 400+", 400, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # CIS_major.add_course("CIS Elective 400+", 400, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # CIS_major.add_course("CIS Elective 300+", 300, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # CIS_major.add_course("CIS Elective 300+", 300, 4, [], [Term("Fall"), Term("Winter"), Term("Spring"), Term("Summer")], is_core = True)
    # # --------------------------------------------------------------------------
    #
    #
    # return CIS_major
