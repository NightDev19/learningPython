from arrow import get


students = {
    1: {"Name": "John", "Age": 20, "Course": "BSIT"},
    2: {"Name": "Jane", "Age": 21, "Course": "BSIT"},
    3: {"Name": "Jenny", "Age": 22, "Course": "BSIT"},
}

def get_student(student_id):
    return students.get(student_id, "Student not found.")


def add_student(id, name, age, course):
    # checking student if exists
    if id in students:
        return "Student ID already exists."
    # adding student
    students[id] = {"Name": name, "Age": age, "Course": course}
    return "Student added successfully."

# Same Concept for add_student function
def update_student(id, name, age, course):
    # checking student if not exists
    if id not in students:
        return "Student not found"
    # updating student
    students[id] = {"Name": name, "Age": age, "Course": course}
    return "Student updated successfully"


def delete_student(student_id):
    if student_id in students:
        del students[student_id]
        return "Student deleted successfully."
    return "Student not found."


def list_students():
    return students


def list_student():
    print("Student Data")
    print("ID\tName\tAge\tCourse")
    for id, data in students.items():
        print(f"{id}\t{data['Name']}\t{data['Age']}\t{data['Course']}")
