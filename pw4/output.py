import curses
import numpy as np

def calculate_gpa(student, courses, marks):
    student_marks = []
    course_credits = []
    for c in courses:
        if c.id in marks and student.id in marks[c.id]:
            student_marks.append(marks[c.id][student.id])
            course_credits.append(c.credits)
            
    if not course_credits:
        return 0.0
        
    marks_arr = np.array(student_marks)
    credits_arr = np.array(course_credits)
    gpa = np.sum(marks_arr * credits_arr) / np.sum(credits_arr)
    return round(gpa, 2)

def sort_students_by_gpa(students, courses, marks):
    for s in students:
        s.gpa = calculate_gpa(s, courses, marks)
    students.sort(key=lambda s: s.gpa, reverse=True)

def show_menu(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 5, "====================================", curses.A_BOLD)
    stdscr.addstr(2, 5, "   STUDENT MANAGEMENT SYSTEM (PW4)  ", curses.A_BOLD)
    stdscr.addstr(3, 5, "====================================", curses.A_BOLD)
    stdscr.addstr(5, 5, "1. Input Students")
    stdscr.addstr(6, 5, "2. Input Courses")
    stdscr.addstr(7, 5, "3. Input Marks")
    stdscr.addstr(8, 5, "4. List Students sorted by GPA")
    stdscr.addstr(9, 5, "0. Exit")
    stdscr.addstr(11, 5, "Select an option: ")
    stdscr.refresh()
    return stdscr.getkey()