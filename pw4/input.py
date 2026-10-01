import math
from domains.student import Student
from domains.course import Course

def input_students(students):
    num = int(input("Enter number of students: "))
    for _ in range(num):
        s_id = input("Enter Student ID: ")
        name = input("Enter Student Name: ")
        dob = input("Enter DoB: ")
        students.append(Student(s_id, name, dob))

def input_courses(courses):
    num = int(input("Enter number of courses: "))
    for _ in range(num):
        c_id = input("Enter Course ID: ")
        name = input("Enter Course Name: ")
        credits = int(input("Enter Credits: "))
        courses.append(Course(c_id, name, credits))

def input_marks(courses, students, marks):
    if not courses or not students:
        print("Please input students and courses first!")
        return
        
    c_id = input("Enter Course ID to input marks: ")
    if c_id not in marks:
        marks[c_id] = {}
    for s in students:
        score = float(input(f"Enter mark for {s.name} (ID: {s.id}): "))
        rounded_score = math.floor(score * 10) / 10
        marks[c_id][s.id] = rounded_score