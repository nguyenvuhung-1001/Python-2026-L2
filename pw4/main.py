import curses
from input import input_students, input_courses, input_marks
from output import show_menu, sort_students_by_gpa

students = []
courses = []
marks = {}

def main(stdscr):
    while True:
        key = show_menu(stdscr)
        curses.endwin()
        
        if key == '1':
            input_students(students)
        elif key == '2':
            input_courses(courses)
        elif key == '3':
            input_marks(courses, students, marks)
        elif key == '4':
            sort_students_by_gpa(students, courses, marks)
            print("\n--- Student List Sorted by GPA ---")
            for s in students:
                print(f"ID: {s.id} | Name: {s.name} | GPA: {s.gpa}")
        elif key == '0':
            print("Exiting program...")
            break
            
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    curses.wrapper(main)