import pytest
import System

#Tests if the program can handle adding a student
def test_add_student(grading_system):
    grading_system.login('goggins', 'augurrox')

    grading_system.usr.add_student('akend3', 'databases')
    grading_system.reload_data()
    courses = grading_system.usr.users["akend3"]['courses']
    assert 'databases' in courses

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem