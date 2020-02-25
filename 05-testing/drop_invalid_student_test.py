import pytest
import System

#Tests if the program can handle a professor dropping a student in a course they don't teach
def test_drop_invalid_student(grading_system):
    grading_system.login('goggins', 'augurrox')

    grading_system.usr.drop_student('akend3', 'comp_sci')
    grading_system.reload_data()
    courses = grading_system.usr.users["akend3"]['courses']
    assert 'comp_sci' in courses

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem