import math
import numpy as np 
import curses
students = []
course = []
marks = {}

def main_ui(stdscr):
    while True:
        stdscr.clear()
        stdscr.addstr(1, 5, "==================", curses.A_BOLD)
        stdscr.addstr(2, 5, "STUDENT MANAGEMENT", curses.A_BOLD)
        stdscr.addstr(3, 5, "==================", curses.A_BOLD)
        stdscr.addstr(5, 5, "1. Input Students")
        stdscr.addstr(6, 5, "2. Input Courses")
        stdscr.addstr(7, 5, "3. Input Marks")
        stdscr.addstr(8, 5, "4. List Students")
        stdscr.addstr(9, 5, "5. List Courses")
        stdscr.addstr(10, 5, "6. Marks")
        stdscr.addstr(11, 5, "7. Sort and show students by GPA")
        stdscr.addstr(12, 5, "0. Exit")
        stdscr.addstr(13, 5, "Enter your choice: ")
        stdscr.refresh()

        curses.endwin()
        
        choice = input()
        if choice == '1':
            input_students()
        elif choice == '2':
            input_courses()
        elif choice == '3':
            input_marks()
        elif choice == '4':
            list_students()
        elif choice == '5':
            list_courses()
        elif choice == '6':
            Marks()
        elif choice == '7':
            sort_student_by_gpa()
        elif choice == '0':
            print("Exiting program")
            break
        else:
            print("Invalid choice!")
            
        input("Press Enter to continue")

def input_number_of_students():
    return int(input("Enter total number of students: "))

def input_students():
    a = input_number_of_students()
    for i in range(a):
        print(f"Student {i+1}")
        student_id = input("Id: ")
        name = input("Name: ")
        DOB = input("DOB: ")
        students.append({'Id': student_id, 'name': name, 'DOB': DOB})

def input_number_of_courses():
    return int(input("Enter total number of courses: "))

def input_courses():
    a = input_number_of_courses()
    for i in range(a):
        print(f"Course {i+1}")
        course_id = input("Id: ")
        name = input("Course name: ")
        credits = int(input("Credits: "))
        course.append({'Id': course_id, 'name': name, 'credits': credits})

def input_marks():
    course_id = input("Enter Course ID to input marks: ")
    marks[course_id] = {}
    for n in students:
        score = float(input(f"Enter mark for {n['name']} (ID: {n['Id']}): "))
        rounded_score = math.floor(score * 10) / 10
        marks[course_id][n['Id']] = rounded_score

def list_courses():
    print("List of courses")
    for c in course:
        print(f"ID: {c['Id']} | Name: {c['name']}")

def list_students():
    print("List of students")
    for n in students:
        print(f"ID: {n['Id']} | Name: {n['name']} | DOB: {n['DOB']}")

def Marks():
    course_id = input("Enter Course ID to view marks: ")
    print(f"Marks for course {course_id}")
    for n in students:
        score = marks[course_id].get(n['Id'], "N/A")
        print(f"Student: {n['name']} | Mark: {score}")

def calculate_gpa(student_id):
    student_marks = []
    course_credits = []
    for c in course:
        c_id = c['Id']
        if c_id in marks and student_id in marks[c_id]:
            student_marks.append(marks[c_id][student_id])
            course_credits.append(c['credits'])
    if not course_credits:
        return 0.0
    
    marks_array = np.array(student_marks)
    credits_array = np.array(course_credits)
    gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)
    return round(gpa, 2)

def sort_student_by_gpa():
    for s in students:
        s['gpa'] = calculate_gpa(s['Id'])
    students.sort(key = lambda s: s['gpa'], reverse=True)
    print("Student list sorted by GPA")
    for s in students:
        print(f"ID: {s['Id']} | Name: {s['name']} | GPA: {s['gpa']}")
  
if __name__ == "__main__":
    curses.wrapper(main_ui)