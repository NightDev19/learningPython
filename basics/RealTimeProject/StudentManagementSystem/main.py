from random import choice
from student_data import *


def main():
    while True:
        print("\n--- Student Management System ---")
        print("1. View Student\n2. Add Student\n3. Update Student\n4. Delete Student\n5. List All Students\n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            id = input("Enter student ID: ")
            print(get_student_data(int(id)))
        elif choice == "2":
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter student course: ")
            print(add_student(id, name, age, course))
        elif choice == "3":
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            age = int(input("Enter student age: "))
            course = input("Enter student course: ")
            print(update_student(id, name, age, course))
        elif choice == "4":
            id = int(input("Enter student ID: "))
            print(delete_student(id))
        elif choice == "5":
            get_all_students()
        elif choice == "6":
            break
        else:
            print("Invalid Choice!")


if __name__ == '__main__':
    main()
