import pytest
import System

#Tests if the program can handle someone creating an assignment in a course they don't teach
def test_create_invalid_assignment(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    course = 'comp_sci'
    grading_system.login(username,password)

    grading_system.usr.create_assignment("test", "2/29/20", course)
    grading_system.reload_data()
    assignments = grading_system.usr.all_courses[course]['assignments']

    assert 'test' not in assignments

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem