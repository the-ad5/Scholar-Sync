import numpy as np
from itertools import combinations

TEACHER_CREDS = [
    ('prof_max', 'grade123'),
    ('dr_anna', 'math_pass')
]

STUDENT_RECORDS = {}

current_user = {'ID_num': '', 'Role': ''}

class User:

    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name

class Student(User):

    def __init__(self, student_id, studentName):
        super().__init__(student_id, studentName)
        self.course_grades = {}

    def calculate_gpa(self):
        # Dummy implementation for now, needs actual GPA calculation logic
        return 3.5 # Placeholder value

    def getGradeLetter(self, score):
        if score >= 90:
            return 'A'
        elif score >= 80:
            return 'B'
        elif score >= 70:
            return 'C'
        elif score >= 60:
            return 'D'
        else:
            return 'F'

def accumulator(scores):
    return sum(scores)

def total(items):
    return len(items)

def power_off():
    print("SCHOLAR-SYNC: Shutting down. Goodbye!")
    # In a real application, you might exit the program here, e.g., exit()

def security():

    print("=="*35)

    print("S C H O L A R - S Y N C")
    print("SCHOLAR-SYNC: EDUCATIONAL HELP SYSTEM v1.1")
    print("Title line made by AADYA SHARMA (Registration ID: 25BCE11123)")
    print("-----------------------------------")

    a = input("Enter option (1: Teacher, 2: Student, 3: Power Off): \t")

    if a == '1':
        teacher_login()
    elif a == '2':
        student_login()
    elif a == '3':
        power_off()
    else:
        security()

def teacher_login():

    user_prompt = input("Enter username: \t")
    pass_prompt = input("Enter password: \t")

    login_ok = False
    for u, p in TEACHER_CREDS:
        if user_prompt == u and pass_prompt == p:
            login_ok = True
            break

    if login_ok:
        current_user['ID_num'] = user_prompt
        current_user['Role'] = 'Teacher'
        teacher_window()
    else:
        security()

def student_login():

    s_id = input("Enter Student ID: \t")

    if s_id in STUDENT_RECORDS:
        current_user['ID_num'] = s_id
        current_user['Role'] = 'Student'
        student_window()
    else:
        print(f"Student ID {s_id} not found. Registering new student...")
        name = input("Enter student's full name: \t")
        STUDENT_RECORDS[s_id] = Student(s_id, name)
        current_user['ID_num'] = s_id
        current_user['Role'] = 'Student'
        student_window()

def teacher_window():

    print("\n"+"***"*10)
    print(f"Welcome Teacher, {current_user['ID_num']}!")
    print("Available Commands:")
    print("--> 1. Enter Student Score")
    print("--> 2. View Class Stats")
    print("--> 3. Advanced Class Analysis")
    print("--> Power")
    print("---"*10)

    a = input("Enter choice: \t")

    if a == '1':
        enter_student_score()
    elif a == '2':
        view_class_stats()
    elif a == '3':
        advanced_class_analysis()
    elif a.lower() == 'power':
        security()
    else:
        teacher_window()

def enter_student_score():

    s_id = input("Enter Student ID: \t")

    if s_id not in STUDENT_RECORDS:
        print(f"Student ID {s_id} not found.")
        teacher_window()
        return

    course_name = input("Enter Course Name: \t")

    try:
        score = float(input("Enter Final Score (0-100): \t"))
        credits = float(input("Enter Credit Hours (3.0): \t"))
    except ValueError:
        print("INPUT ERROR. Must be numbers.")
        teacher_window()
        return

    STUDENT_RECORDS[s_id].course_grades[course_name] = {
        'credits': credits,
        'finalScore': score
    }
    print(f"Score {score} recorded for ID {s_id}.")
    teacher_window()


def view_class_stats():

    course_name = input("Enter course name to analyze: \t")
    scores_list = []

    for s_obj in STUDENT_RECORDS.values():
        if course_name in s_obj.course_grades:
            scores_list.append(s_obj.course_grades[course_name]['finalScore'])

    if not scores_list:
        print(f"No scores found for course '{course_name}'.")
        teacher_window()
        return

    total_score = accumulator(scores_list)
    student_count = total(scores_list)
    class_average = total_score / student_count

    temp_student = Student("TEMP_ID", "Grader")
    class_letter = temp_student.getGradeLetter(class_average)

    print(f"CLASS average: {class_average:.2f}% | GRADE: {class_letter}")
    teacher_window()
def advanced_class_analysis():

    print("\n\n*** ADVANCED CLASS ENROLLMENT & STATS ***\n")

    MATH_ENROLLED_SET = {'25BCE11123', '25BCE0001', '25BCE0002', 'Ram', 'Shyam'}
    CS_ENROLLED_SET = {'25BCE11123', '25BCE0003', '25BCE0004', 'Suraj', 'Ram'}

    combined_enrollment = MATH_ENROLLED_SET.union(CS_ENROLLED_SET)
    frozen_unique = frozenset(combined_enrollment)

    Set_Length = total(frozen_unique)
    print(f"Total Unique Students in Math/CS Combined: {Set_Length}")

    only_in_math = MATH_ENROLLED_SET.difference(CS_ENROLLED_SET)
    print(f"Students ONLY in Math: {only_in_math}")

    # Note: numpy.array.accumulator() is not a valid method. Assuming a custom accumulator function is intended.
    # Also, need to handle case where 'Python Essentials' might not be present.
    scores_for_python = np.array([s_obj.course_grades.get('Python Essentials', {}).get('finalScore', 0)
                              for s_obj in STUDENT_RECORDS.values()])

    if scores_for_python.size > 0 and accumulator(scores_for_python) > 0: # Using the custom accumulator function
        std_dev = np.std(scores_for_python)
        print(f"\npython Scores Standard Deviation: {std_dev:.2f}")
    else:
        print("\nNOTE: Insufficient data for Python Scores Standard Deviation.")

    top_students = ['Ram', 'Shyam', 'Suraj', 'Vipul']
    project_groups = list(combinations(top_students, 3))
    print(f"\nPossible 3-person Group Combinations: {project_groups}")

    teacher_window()

def student_window():

    student_obj = STUDENT_RECORDS[current_user['ID_num']]

    print("\n"+"***"*10)
    print(f"Hi, {student_obj.user_name}!")
    print("Available Commands:")
    print("--> 1. View My Grades")
    print("--> 2. Calculate My GPA")
    print("--> Power")
    print("---"*10)

    a = input("Enter choice: \t")

    if a == '1':
        view_my_grades(student_obj)
    elif a == '2':
        calculate_my_gpa(student_obj)
    elif a.lower() == 'power':
        security()
    else:
        student_window()

def view_my_grades(student_obj):
    print("\n--- Your Grades ---")
    if not student_obj.course_grades:
        print("No grades recorded yet.")
        student_window()
        return

    for course, details in student_obj.course_grades.items():
        score = details['finalScore']
        credits = details['credits']
        letter_grade = student_obj.getGradeLetter(score)
        print(f"Course: {course} | Score: {score:.2f} | Credits: {credits:.1f} | Grade: {letter_grade}")
    student_window()

def calculate_my_gpa(student_obj):

    gpa = student_obj.calculate_gpa()

    print("\n--- Your GPA Summary ---")
    print(f"YOUR CUMULATIVE GPA IS: {gpa:.2f}")

    student_window()

def power():

    print("SYSTEM INITIALIZING...")
    a = input('-->[ON/OFF]\t')
    if a.upper() == 'ON':
        security()
    elif a.upper() == 'OFF':
        power_off()
    else:
        power()

if __name__ == "__main__":
    STUDENT_RECORDS['25BCE11123'] = Student('25BCE11123', 'AADYA SHARMA')
    STUDENT_RECORDS['25BCE11123'].course_grades['Python Essentials'] = {'credits': 4.0, 'finalScore': 92.5}
    STUDENT_RECORDS['25BCE0001'] = Student('25BCE0001', 'Test Student 1')
    STUDENT_RECORDS['25BCE0001'].course_grades['Python Essentials'] = {'credits': 4.0, 'finalScore': 85.0}

    power()
