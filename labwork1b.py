students = []
course = []
marks = {}

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
        course.append({'Id': course_id, 'name': name})

def input_marks():
    course_id = input("Enter Course ID to input marks: ")
    marks[course_id] = {}
    for n in students:
        score = float(input(f"Enter mark for {n['name']} (ID: {n['Id']}): "))
        marks[course_id][n['Id']] = score

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

input_students()  
input_courses()   

list_students()   
list_courses()    

input_marks()     
Marks()           