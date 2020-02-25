import pytest
import System

#Tests if the program can handle changing a grade
def test_grade_change(grading_system):
    username = 'cmhbf5'
    password = 'bestTA'
    grading_system.login(username,password)
    grading_system.usr.change_grade('yted91', 'cloud_computing', 'assignment1', 24)
    grading_system.reload_data()
    assert grading_system.usr.users['yted91']['courses']['cloud_computing']['assignment1']['grade'] == 24


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem