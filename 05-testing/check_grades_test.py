import pytest
import System

#Tests if the program can check grades correctly
def test_check_grades(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'cloud_computing'
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