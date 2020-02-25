import pytest
import System

#Tests if the program can handle a student attempting to check grades in a course they don't take
def test_check_invalid_grades(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'comp_sci'
    grading_system.login(username, password)

    grades = grading_system.usr.check_grades(course)
    assignments = grading_system.usr.users[username]['courses'][course]
    check_grades = []
    for key in assignments:
        check_grades.append([key, assignments[key]['grade']])
    
    assert grades == check_grades


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem