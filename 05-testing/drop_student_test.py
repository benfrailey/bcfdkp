import pytest
import System

#Tests if the program can handle a dropped student
def test_drop_student(grading_system):
    grading_system.login('goggins', 'augurrox')

    grading_system.usr.drop_student('akend3', 'databases')
    grading_system.reload_data()
    courses = grading_system.usr.users["akend3"]['courses']
    assert 'databases' not in courses

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem