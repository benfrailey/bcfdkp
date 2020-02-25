import pytest
import System

#Tests if the program can handle creating an assignment
def test_create_assignment(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    course = 'software_engineering'
    grading_system.login(username,password)

    grading_system.usr.create_assignment("test", "2/29/20", course)
    grading_system.reload_data()
    assignments = grading_system.usr.all_courses[course]['assignments']

    assert 'test' in assignments

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem