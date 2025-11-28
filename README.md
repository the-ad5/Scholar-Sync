SCHOLAR-SYNC: Educational Help System v1.1

Project Overview
SCHOLAR-SYNC is a command-line Educational Help System designed to manage student records, process course grades, and perform fundamental class statistics. The project serves as a practical application of Object-Oriented Programming (OOP) in Python, utilizing standard data structures and external libraries for robust academic data processing. The system implements distinct, role-based login views for Teachers and Students to ensure controlled data access and security.

Features (Functional Modules)
The system incorporates the required three major functional modules:

User Management and Authentication:

Implements role-based login mechanisms for Teachers and Students.

Includes logic for immediate student registration upon first login attempt if the ID is not found.

Data Processing and Grade Management:

Teachers can input final scores and credit hours for specific courses (enter_student_score).

Calculates and returns letter grades based on the numeric score.

Reporting and Analytics:

Class Statistics: Calculates class averages and converts the average score to a letter grade (view_class_stats).

Advanced Analysis: Performs enrollment set operations (Union, Difference) and uses NumPy to calculate the Standard Deviation of scores.

Team Generation: Generates all possible project team combinations using combinatorial algorithms (advanced_class_analysis).

Technologies and Tools Used
The following technologies and tools were utilized in the development of this project:

Programming Language: Python 3.x

External Libraries: NumPy, itertools

Data Storage: Dictionary-based data structures simulating file storage.

Version Control: Git & GitHub

Architectural Pattern: Simple Modular Design (Function-based flow with OOP for data entities)

Steps to Install and Run the Project
This section provides a clear, logical workflow for interacting with the system.

Clone the Repository: Use the git clone command and navigate into the project directory. git clone https://github.com/dev-pd-1525/brain-bridge.git

Install Dependencies: Install the required numerical library. pip install numpy

Execute the Main Application File: python main.py

Initial Credentials (Example):

Teacher: prof_max / grade123

Student (Pre-loaded): 25BCE11123

Instructions for Testing
Follow these steps to validate core functionality and demonstrate error handling:

Functional Verification: Log in as a Teacher and successfully use the score entry and class stats features, confirming output accuracy.

Access Control Testing (Security NFR): Log in as a Student. Attempt to execute a Teacher-only command. The system must restrict access and return to the student menu.

Error Handling Testing (Robustness NFR): Log in as a Teacher. When prompted for "Final Score," input non-numeric data (e.g., "score"). The system must correctly display "INPUT ERROR. Must be numbers."
