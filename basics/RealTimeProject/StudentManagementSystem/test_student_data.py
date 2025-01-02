# test_student_data.py
import pytest
from student_data import *

# Test data setup


@pytest.fixture
def setup_students():
    # Reset students dictionary before each test
    students.clear()
    students.update({
        1: {"Name": "Alice", "Age": 21, "Course": "BSCS"},
        2: {"Name": "Bob", "Age": 22, "Course": "BSIT"},
    })
    return students

# Test get_student function


def test_get_student(setup_students):
    assert get_student(1) == {"Name": "Alice", "Age": 21, "Course": "BSCS"}
    assert get_student(3) == "Student not found."

# Test add_student function


def test_add_student(setup_students):
    assert add_student(3, "Charlie", 20, "BSCE") == "Student added successfully."
    assert students[3] == {"Name": "Charlie", "Age": 20, "Course": "BSCE"}
    assert add_student(1, "Alice", 21, "BSCS") == "Student ID already exists."

# Test delete_student function


def test_delete_student(setup_students):
    assert delete_student(1) == "Student deleted successfully."
    assert 1 not in students
    assert delete_student(3) == "Student not found."

# Test list_students function


def test_list_students(setup_students):
    all_students = list_students()
    assert len(all_students) == 2
    assert all_students[1] == {"Name": "Alice", "Age": 21, "Course": "BSCS"}
    assert all_students[2] == {"Name": "Bob", "Age": 22, "Course": "BSIT"}
