# Scholar-Sync
A simple console-based “Scholar-Sync” system for teachers and students. Supports login, student registration, course score entry, grade letters, and basic GPA view. Includes class stats, set-based enrollment analysis, NumPy standard deviation for Python scores, and project group combinations via itertools.
# SCHOLAR-SYNC: Educational Help System v1.1 
Made By:Aadya Sharma
reg. id:25BCE11123

## Overview
SCHOLAR-SYNC is a command-line application that serves as a basic educational management system, allowing faculty to manage student records and scores, and students to access their individual performance data. It demonstrates core Python concepts, including Object-Oriented Programming (OOP), function modularity, and use of external libraries like NumPy and itertools for data processing and analysis.

## Features 
* Role-Based Access Control (Teacher/Student): Teachers log in with credentials; students log in via ID.
* Student Registration: Automatically registers a new student if their ID is not found upon first login.
* Grade Entry & Storage: Teachers can input and store final scores and credit hours for various courses.
* Class Statistics: Calculates the overall class average and assigns a corresponding letter grade for any recorded course.
* Advanced Analysis: Performs set operations (`union`, `difference`) on pre-defined course enrollment sets (Math/CS) and calculates the **Standard Deviation** of scores for a specific course (Python Essentials).
* Combinatorial Analysis: Uses `itertools.combinations` to generate possible 3-person project groups.
* Grade Reporting: Displays a student's individual course scores, credits, and calculated letter grades.

## Technologies/Tools Used 
* Core Language: Python 3.x
* Libraries: `numpy` (for statistical calculation), `itertools` (for combinatorial mathematics).

## Steps to Install & Run the Project
1.  Prerequisites: Ensure Python 3.x is installed on your operating system.
2.  Install Dependencies: Install the required external library via pip:
    ```bash
    pip install numpy
    ```
3.  Setup: Save the entire provided source code into a single Python file (e.g., `scholar_sync.py`).
4.  Run Application: Execute the file from your terminal:
    ```bash
    python scholar_sync.py
    ```
5.  Initiate: Enter `ON` when prompted at the system initialization screen to start the main menu.

## Instructions for Testing 
1.  Teacher Login: Use the credentials `prof_max` / `grade123` to access the Teacher Menu.
2.  Student Login (Existing): Use ID `25BCE11123` to access the Student Menu.
3.  Test Score Entry: As a Teacher (Command 1), enter a new score for student `25BCE0001` in a course like 'Chemistry 101'.
4.  Test Class Stats: As a Teacher (Command 2), analyze 'Python Essentials' to confirm the class average calculation (should be 88.75).
5.  Test Grade View: As a Student (Command 1), view grades to confirm the letter grade calculation (92.5 -> A).
