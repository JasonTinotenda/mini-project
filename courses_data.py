"""
courses_data.py

This module contains a nested dictionary structure that stores course
information organized by academic program and level.

Structure:
{
  "Program Name": {
      "Level 1": [
          {"code": "XXX101", "name": "Course Name", "credits": 3},
          ...
      ],
      "Level 2": [...],
      ...
  },
  ...
}

Example access:
    from courses_data import COURSES
    cs_level1 = COURSES["Computer Science"]["Level 1"]
    for course in cs_level1:
        print(course["code"], course["name"], course["credits"])

Feel free to extend programs, levels or add more fields to each course.
"""

# Dictionary containing program metadata and detailed module listings
COURSES = {
    "Computer Science": {
        "career_opportunities": (
            "Research Scientists, IT Managers, IT Consultants, Software Engineers, "
            "Analyst Programmers, Systems Analysts, Security Analysts, Website Designers, "
            "Website Developers, Database Administrators, Network and Systems Administrators, "
            "and Hardware Technicians."
        ),
        "further_studies": (
            "Master's and doctoral studies in Computer Science or in interdisciplinary "
            "programmes related to computing practices."
        ),
        "programme_notes": (
            "A student will not be allowed to register for a module with a pre-requisite "
            "if the pre-requisite is not passed. Electives will be offered subject to the "
            "availability of personnel. '*' denotes core modules."
        ),
        "levels": {
            "Level 1": {
                "Semester 1": [
                    {"code": "HCSCI131", "name": "Introduction to Computers and Computer Applications", "credits": 10, "core": True},
                    {"code": "HCSCI132", "name": "Principles of Programming Languages", "credits": 10, "core": True},
                    {"code": "HCSCI133", "name": "Operating Systems", "credits": 10, "core": True},
                    {"code": "HCSCI134", "name": "Fundamentals of Digital Electronics", "credits": 10, "core": True},
                    {"code": "HCSE133", "name": "Ethics and Professionalism", "credits": 10, "core": True},
                    {"code": "CS131", "name": "Basics of Communication Skills", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSCI135", "name": "Computer Architecture and Organization", "credits": 10, "core": True},
                    {"code": "HCSCI136", "name": "Data Structures and Algorithms", "credits": 10, "core": True},
                    {"code": "HCSCI137", "name": "Software Engineering", "credits": 10, "core": True},
                    {"code": "HCSE135", "name": "Database Systems", "credits": 10, "core": True},
                    {"code": "HCSE138", "name": "Discrete Mathematics", "credits": 10, "core": True},
                    {"code": "HTENG133", "name": "Physics for Engineers", "credits": 10, "core": False},
                ],
            },

            "Level 2": {
                "Semester 1": [
                    {"code": "HCSCI231", "name": "Web Development", "credits": 10, "core": True},
                    {"code": "HCSCI232", "name": "Systems Analysis and Design", "credits": 10, "core": True},
                    {"code": "HCSCI233", "name": "Computer Security", "credits": 10, "core": False},
                    {"code": "HCSCI234", "name": "Research Methods", "credits": 10, "core": True},
                    {"code": "HSTA132", "name": "Applied Statistics", "credits": 12, "core": True},
                    {"code": "GS231", "name": "Gender Studies", "credits": 12, "core": True},
                    {"code": "TCNP201", "name": "Technopreneurship", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSCI235", "name": "Software Project Management", "prerequisite": "HCSCI137", "credits": 10, "core": True},
                    {"code": "HCSCI237", "name": "Data Communications and Computer Networks", "credits": 10, "core": True},
                    {"code": "HCSCI238", "name": "Design and Analysis of Algorithms", "prerequisite": "HCSCI136", "credits": 10, "core": True},
                    {"code": "HCSCI239", "name": "Digital Image Processing", "credits": 10, "core": False},
                    {"code": "HCSCI240", "name": "Group Project", "prerequisite": "HCSCI232", "credits": 10, "core": True},
                    {"code": "HCSE224", "name": "Object Oriented Programming", "prerequisite": "HCSCI132", "credits": 10, "core": True},
                ],
            },

            "Level 3": {
                "Semester 1": [
                    {"code": "HCSCI311", "name": "Work-Related Learning I", "credits": 40, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSCI321", "name": "Work-Related Learning II", "prerequisite": "HCSCI311", "credits": 80, "core": True},
                ],
            },

            "Level 4": {
                "Semester 1": [
                    {"code": "HCSCI431", "name": "Theory of Computation", "credits": 10, "core": True},
                    {"code": "HCSCI432", "name": "Simulation and Modelling", "credits": 10, "core": True},
                    {"code": "HCSCI433", "name": "Parallel and Distributed Computing", "prerequisite": "HCSCI237", "credits": 10, "core": True},
                    {"code": "HCSCI434", "name": "Artificial Intelligence", "credits": 10, "core": True},
                    {"code": "HTENG432", "name": "Communications Network Design", "prerequisite": "HCSCI237", "credits": 10, "core": True},
                ],
                "Semester 1 Electives": [
                    {"code": "HCSE433", "name": "IoT and Cloud Systems Engineering", "prerequisite": "HCSCI237", "credits": 10, "core": False},
                    {"code": "HCSE434", "name": "Machine Learning", "credits": 10, "core": False},
                    {"code": "HCSE435", "name": "Digital Media Engineering", "credits": 10, "core": False},
                ],
                "Semester 2": [
                    {"code": "HCSCI435", "name": "Computer Graphics", "credits": 10, "core": True},
                    {"code": "HCSCI437", "name": "Human Computer Interaction", "credits": 10, "core": True},
                    {"code": "HCSCI438", "name": "Research Project", "prerequisite": "HCSCI240", "credits": 20, "core": True},
                    {"code": "HCSE439", "name": "Network Security and Cryptography", "credits": 10, "core": True},
                ],
                "Semester 2 Electives": [
                    {"code": "HCSCI439", "name": "Fundamentals of Data Science and Big Data", "credits": 10, "core": False},
                    {"code": "HCSCI436", "name": "Information Security", "credits": 10, "core": False},
                ],
            },
        },
    },

    "Computer Engineering": {
        "career_opportunities": (
            "Software Engineers, Network Engineers, Hardware Engineers, Website Designers, "
            "Analyst Programmers, Network and Systems Administrators, Database Administrators, "
            "IT Managers, and Systems Analysts."
        ),
        "further_studies": (
            "Master's and doctoral studies in Computer Systems Engineering, Computer Science, "
            "Data Science, or interdisciplinary programmes related to computing practices."
        ),
        "programme_notes": (
            "A student will not be allowed to register for a module with a pre-requisite "
            "if the pre-requisite is not passed. Electives will be offered subject to availability "
            "of personnel. '*' denotes core modules."
        ),
        "levels": {
            "Level 1": {
                "Semester 1": [
                    {"code": "HCSE131", "name": "Introduction to Computer Engineering", "credits": 10, "core": True},
                    {"code": "HCSE133", "name": "Ethics and Professionalism", "credits": 10, "core": True},
                    {"code": "HCSCI132", "name": "Principles of Programming Languages", "credits": 10, "core": True},
                    {"code": "HTENG133", "name": "Physics for Engineers", "credits": 10, "core": True},
                    {"code": "HMAT131", "name": "Calculus 1", "credits": 12, "core": True},
                    {"code": "CS131", "name": "Basics of Communication Skills", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSE134", "name": "Electrical and Electronic Principles", "credits": 10, "core": True},
                    {"code": "HCSE135", "name": "Database Systems", "credits": 10, "core": True},
                    {"code": "HCSCI136", "name": "Data Structures and Algorithms", "credits": 10, "core": True},
                    {"code": "HCSE137", "name": "Digital Electronics and Logic Design", "credits": 10, "core": True},
                    {"code": "HCSE138", "name": "Discrete Mathematics", "credits": 10, "core": True},
                    {"code": "HCSCI137", "name": "Software Engineering", "credits": 10, "core": True},
                ],
            },

            "Level 2": {
                "Semester 1": [
                    {"code": "HCSE231", "name": "Object Oriented Analysis and Design", "credits": 10, "core": True},
                    {"code": "HCSE232", "name": "Engineering Statistics", "credits": 10, "core": True},
                    {"code": "HCSE233", "name": "Linear Algebra", "credits": 10, "core": True},
                    {"code": "HCSCI133", "name": "Operating Systems", "credits": 10, "core": True},
                    {"code": "HCSCI135", "name": "Computer Architecture and Organization", "credits": 10, "core": True},
                    {"code": "GS231", "name": "Gender Studies", "credits": 12, "core": True},
                    {"code": "TCNP201", "name": "Technopreneurship", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSE224", "name": "Object Oriented Programming", "prerequisite": "HCSE231", "credits": 10, "core": True},
                    {"code": "HCSE235", "name": "Web and Mobile Application Development", "credits": 10, "core": False},
                    {"code": "HCSE236", "name": "Group Project", "prerequisite": "HCSE231", "credits": 10, "core": True},
                    {"code": "HCSCI237", "name": "Data Communications and Computer Networks", "credits": 10, "core": True},
                    {"code": "HCSCI238", "name": "Design and Analysis of Algorithms", "prerequisite": "HCSCI136", "credits": 10, "core": True},
                    {"code": "HTENG237", "name": "Digital Signal Processing", "credits": 10, "core": False},
                ],
            },

            "Level 3": {
                "Semester 1": [
                    {"code": "HCSE311", "name": "Work-Related Learning I", "credits": 40, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSE321", "name": "Work-Related Learning II", "prerequisite": "HCSE311", "credits": 80, "core": True},
                ],
            },

            "Level 4": {
                "Semester 1": [
                    {"code": "HCSE431", "name": "Microprocessors and Microcontrollers Systems", "prerequisite": "HCSE134", "credits": 10, "core": True},
                    {"code": "HCSE432", "name": "Embedded Systems", "prerequisite": "HCSCI135", "credits": 10, "core": True},
                    {"code": "HCSCI234", "name": "Research Methods", "credits": 10, "core": True},
                    {"code": "HCSCI433", "name": "Parallel and Distributed Computing", "prerequisite": "HCSE137", "credits": 10, "core": True},
                    {"code": "HTENG432", "name": "Communications Network Design", "prerequisite": "HCSCI237", "credits": 10, "core": True},
                ],
                "Semester 1 Electives": [
                    {"code": "HCSE433", "name": "IoT and Cloud Systems Engineering", "prerequisite": "HCSCI237", "credits": 10, "core": False},
                    {"code": "HCSE434", "name": "Machine Learning", "credits": 10, "core": False},
                    {"code": "HCSE435", "name": "Digital Media Engineering", "credits": 10, "core": False},
                ],
                "Semester 2": [
                    {"code": "HCSE436", "name": "Control Systems Engineering", "credits": 10, "core": True},
                    {"code": "HCSE439", "name": "Network Security and Cryptography", "credits": 10, "core": True},
                    {"code": "HCSE437", "name": "Project Management", "prerequisite": "HCSCI137", "credits": 10, "core": True},
                    {"code": "HCSE438", "name": "Research Project", "prerequisite": "HCSE236", "credits": 10, "core": True},
                ],
                "Semester 2 Electives": [
                    {"code": "HCSCI439", "name": "Fundamentals of Data Science and Big Data", "prerequisite": "HCSE135", "credits": 10, "core": False},
                    {"code": "HCSCI436", "name": "Information Security", "credits": 0, "core": False},
                ],
            },
        },
    },

    "Cybersecurity": {
        "career_opportunities": (
            "Research Scientists, Information Security Analyst, Lead Software Security Engineer, "
            "Chief Information Security Officer, Analyst Programmers, Penetration Tester, "
            "Cybersecurity Crime Investigator/Forensics Expert"
        ),
        "further_studies": (
            "Master's and doctoral studies in Cybersecurity or in interdisciplinary programmes "
            "related to computing practices."
        ),
        "programme_notes": (
            "A student will not be allowed to register for a module with a pre-requisite "
            "if the pre-requisite is not passed. Electives will be offered subject to availability "
            "of personnel. '*' denotes core modules."
        ),
        "levels": {
            "Level 1": {
                "Semester 1": [
                    {"code": "HCSCI132", "name": "Fundamentals of Programming Languages", "credits": 10, "core": True},
                    {"code": "HSWE111", "name": "Software Engineering Fundamentals", "credits": 10, "core": True},
                    {"code": "HCSCI133", "name": "Operating Systems", "credits": 10, "core": True},
                    {"code": "HCSEC111", "name": "Introduction to Information Security", "credits": 10, "core": True},
                    {"code": "HCSE138", "name": "Discrete Mathematics", "credits": 10, "core": True},
                    {"code": "CS131", "name": "Communication Skills", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSCI135", "name": "Computer Architecture and Organization", "credits": 10, "core": False},
                    {"code": "HCSEC122", "name": "Cyberspace Ethics and Laws", "credits": 10, "core": True},
                    {"code": "HCSEC123", "name": "Principles of Secure Coding", "credits": 10, "core": True},
                    {"code": "HCSE135", "name": "Database Systems", "credits": 10, "core": False},
                    {"code": "HCSCI136", "name": "Data Structures and Algorithms", "credits": 10, "core": True},
                    {"code": "HCSEC125", "name": "Forensics and Incident Response", "credits": 10, "core": True},
                ],
            },
            "Level 2": {
                "Semester 1": [
                    {"code": "HCSEC211", "name": "Coding Theory", "prerequisite": "HCSE138", "credits": 10, "core": True},
                    {"code": "HCSEC212", "name": "Number Theory", "prerequisite": "HCSE138", "credits": 10, "core": True},
                    {"code": "HCSCI234", "name": "Research Methods", "credits": 10, "core": True},
                    {"code": "HCSCI237", "name": "Data Communications and Computer Networks", "credits": 10, "core": False},
                    {"code": "TNCP201", "name": "Technopreneurship", "credits": 12, "core": True},
                    {"code": "GS231", "name": "Gender Studies", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSEC221", "name": "Network Programming", "prerequisite": "HCSEC123", "credits": 10, "core": True},
                    {"code": "HCSEC222", "name": "Cryptography", "prerequisite": "HCSEC111", "credits": 10, "core": True},
                    {"code": "HCSEC223", "name": "Ethical Hacking", "credits": 10, "core": True},
                    {"code": "HCSEC224", "name": "Cybersecurity Mini Project", "credits": 12, "core": True},
                ],
                "Electives": [
                    {"code": "HSWE221", "name": "Web Technologies", "credits": 10, "core": False},
                    {"code": "HCSEC225", "name": "Systems Administration and Security", "credits": 10, "core": False},
                ],
            },
            "Level 3": {
                "Semester 1": [
                    {"code": "HCSEC311", "name": "Work-Related Learning I", "credits": 40, "core": True},
                ],
                "Semester 2": [
                    {"code": "HCSEC321", "name": "Work-Related Learning II", "prerequisite": "HCSEC311", "credits": 80, "core": True},
                ],
            },
            "Level 4": {
                "Semester 1": [
                    {"code": "HCSEC411", "name": "Blockchain Technology", "credits": 10, "core": True},
                    {"code": "HCSEC412", "name": "Network Security", "prerequisite": "HCSEC221", "credits": 10, "core": True},
                    {"code": "HCSEC413", "name": "Digital Forensics", "prerequisite": "HCSEC125", "credits": 10, "core": True},
                    {"code": "HCSEC414", "name": "Cryptanalysis and Development of Cryptosystems", "prerequisite": "HCSEC222", "credits": 10, "core": True},
                    {"code": "HCSEC415", "name": "Cybercrime and Security Management", "credits": 10, "core": True},
                ],
                "Electives": [
                    {"code": "HCSEC416", "name": "Secure Ecommerce", "credits": 10, "core": False},
                    {"code": "HSWE419", "name": "Advanced Web Engineering", "prerequisite": "HSWE221", "credits": 10, "core": False},
                    {"code": "HSWE418", "name": "Web Services and Service Oriented Architecture", "credits": 10, "core": False},
                ],
                "Semester 2": [
                    {"code": "HCSEC421", "name": "Android Security Design and Internals", "credits": 10, "core": True},
                    {"code": "HCSEC422", "name": "Cloud Architectures and Security", "prerequisite": "HSWE221", "credits": 10, "core": True},
                    {"code": "HCSEC423", "name": "IT Auditing and Assurance", "credits": 10, "core": True},
                    {"code": "HCSEC424", "name": "Penetration Testing and Vulnerability Assessment", "prerequisite": "HCSEC125, HCSEC223", "credits": 10, "core": True},
                    {"code": "HCSEC425", "name": "Capstone Project", "prerequisite": "HCSEC224", "credits": 24, "core": True},
                ],
            },
        },
    },

    "Software Engineering": {
        "career_opportunities": (
            "Software Architect, Software Developer, Systems Analyst, Systems Engineer, Software Tester, "
            "Information Systems Managers, Cloud Manager, Database Engineer, Data Scientist, Network Engineer, "
            "Software Project Manager."
        ),
        "further_studies": (
            "Masters and Doctoral studies in Software Engineering, Data Science, Cloud Computing, Information Security "
            "and any other relevant Computing discipline."
        ),
        "programme_notes": (
            "A student will not be allowed to register for a module with a pre-requisite "
            "if the pre-requisite is not passed. Electives will be offered subject to the availability "
            "of personnel. '*' denotes core modules."
        ),
        "levels": {
            "Level 1": {
                "Semester 1": [
                    {"code": "HSWE111", "name": "Software Engineering Fundamentals", "credits": 10, "core": True},
                    {"code": "HCSCI132", "name": "Principles of Programming Languages", "credits": 10, "core": True},
                    {"code": "HCSCI133", "name": "Operating Systems", "credits": 10, "core": True},
                    {"code": "HCSCI136", "name": "Data Structures and Algorithms", "credits": 10, "core": True},
                    {"code": "HCSE138", "name": "Discrete Mathematics", "credits": 10, "core": False},
                    {"code": "CS131", "name": "Basics of Communication Skills", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HSWE121", "name": "Visual Programming", "credits": 10, "core": True},
                    {"code": "HSWE122", "name": "Computer Networks and Information Security", "credits": 10, "core": True},
                    {"code": "HSTA132", "name": "Applied Statistics", "credits": 10, "core": True},
                    {"code": "HCSE133", "name": "Ethics and Professionalism", "credits": 10, "core": True},
                    {"code": "HCSCI135", "name": "Computer Architecture and Organization", "credits": 10, "core": True},
                    {"code": "HCSE135", "name": "Database Systems", "credits": 10, "core": True},
                ],
            },
            "Level 2": {
                "Semester 1": [
                    {"code": "HCSE224", "name": "Object Oriented Programming", "prerequisite": "HCSCI132", "credits": 10, "core": True},
                    {"code": "HSWE212", "name": "Requirements Engineering", "credits": 10, "core": True},
                    {"code": "HCSCI235", "name": "Software Project Management", "prerequisite": "HSWE111", "credits": 10, "core": True},
                    {"code": "HCSCI234", "name": "Research Methods", "credits": 10, "core": True},
                    {"code": "GS231", "name": "Gender Studies", "credits": 12, "core": True},
                    {"code": "TCNP201", "name": "Technopreneurship", "credits": 12, "core": True},
                ],
                "Semester 2": [
                    {"code": "HSWE221", "name": "Web Technologies", "credits": 10, "core": True},
                    {"code": "HSWE222", "name": "Software Architecture and Design", "credits": 10, "core": True},
                    {"code": "HSWE223", "name": "Advanced Database Systems", "prerequisite": "HCSE135", "credits": 10, "core": True},
                    {"code": "HSWE224", "name": "Mini Project", "credits": 10, "core": True},
                ],
                "Electives": [
                    {"code": "HSWE225", "name": "Mobile Application Development", "prerequisite": "HCSE224", "credits": 10, "core": False},
                    {"code": "HSWE226", "name": "Game Programming", "prerequisite": "HCSE224", "credits": 10, "core": False},
                ],
            },
            "Level 3": {
                "Semester 1": [
                    {"code": "HSWE311", "name": "Work-Related Learning I", "credits": 40, "core": True},
                ],
                "Semester 2": [
                    {"code": "HSWE321", "name": "Work-Related Learning II", "prerequisite": "HSWE311", "credits": 80, "core": True},
                ],
            },
            "Level 4": {
                "Semester 1": [
                    {"code": "HSWE411", "name": "Software Testing and Quality Assurance", "prerequisite": "HSWE111", "credits": 10, "core": True},
                    {"code": "HSWE412", "name": "Software Evolution and Re-engineering", "prerequisite": "HSWE212", "credits": 10, "core": True},
                    {"code": "HCSCI437", "name": "Human Computer Interaction", "credits": 10, "core": True},
                    {"code": "HCSCI432", "name": "Simulation and Modelling", "prerequisite": "HSTA132", "credits": 10, "core": True},
                ],
                "Elective 1": [
                    {"code": "HSWE415", "name": "Mobile Computing and Wireless Networks", "prerequisite": "HSWE122", "credits": 10, "core": False},
                    {"code": "HSWE416", "name": "IoT and Cloud Computing", "prerequisite": "HSWE122", "credits": 10, "core": False},
                    {"code": "HCSCI433", "name": "Parallel and Distributed Computing", "prerequisite": "HSWE122", "credits": 10, "core": False},
                ],
                "Elective 2": [
                    {"code": "HSWE418", "name": "Web Services and Service-Oriented Architecture", "prerequisite": "HSWE221", "credits": 10, "core": False},
                    {"code": "HSWE419", "name": "Advanced Web Engineering", "prerequisite": "HSWE221", "credits": 10, "core": False},
                    {"code": "HSWE420", "name": "Image Processing and Machine Vision", "credits": 10, "core": False},
                ],
                "Semester 2": [
                    {"code": "HCSCI431", "name": "Theory of Computation", "credits": 10, "core": True},
                    {"code": "HCSE439", "name": "Network Security and Cryptography", "credits": 10, "core": True},
                    {"code": "HCSCI434", "name": "Artificial Intelligence", "credits": 10, "core": True},
                    {"code": "HSWE424", "name": "Data Science and Big Data Analytics", "credits": 10, "core": True},
                    {"code": "HSWE425", "name": "Capstone Project", "prerequisite": "HSWE214, HSWE224", "credits": 24, "core": True},
                ],
            },
        },
    },
}
