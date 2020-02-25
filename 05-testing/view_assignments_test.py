import pytest
import System

#Tests if the program can view assignments properly
def test_view_assignments(grading_system):
    username = 'akend3'
    password = '123454321'
    course = 'cloud_computing'
    grading_system.login(username, password)

    final_assignments = []
    assignments = grading_system.usr.view_assignments(course)
    check_assignments = grading_system.usr.all_courses[course]['assignments']
    for key in check_assignments:
        final_assignments.append([key,check_assignments[key]['due_date']])
    
    assert assignments == final_assignments


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem