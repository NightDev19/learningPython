from arrow import get


students = {
    1: {"Name": "John", "Age": 20, "Course": "BSIT"},
    2: {"Name": "Jane", "Age": 21, "Course": "BSIT"},
    3: {"Name": "Jenny", "Age": 22, "Course": "BSIT"},
}


def get_student_data(id):
    data = students.get(id)
    if not data:
        return "Student not found"
    return f"ID\tName\tAge\tCourse\n{id}\t{data['Name']}\t{data['Age']}\t{data['Course']}"


def add_student(id, name, age, course):
    # checking student if exists
    if id in students:
        return "Student already exists"
    # adding student
    students[id] = {"Name": name, "Age": age, "Course": course}
    return "Student added successfully"

# Same Concept for add_student function


def update_student(id, name, age, course):
    # checking student if not exists
    if id not in students:
        return "Student not found"
    # updating student
    students[id] = {"Name": name, "Age": age, "Course": course}
    return "Student updated successfully"


def delete_student(id):
    # checking student if not exists
    if id not in students:
        return "Student not found"
    # deleting student
    del students[id]  # using the principle of del() function of list
    return "Student deleted successfully"


def get_all_students():
    print("Student Data")
    print("ID\tName\tAge\tCourse")
    for id, data in students.items():
        print(f"{id}\t{data['Name']}\t{data['Age']}\t{data['Course']}")
