import pytest
import System

#Tests if the program can handle submitting an assignment
def test_submit_assignment(grading_system):
    username = 'hdjsr7'
    password = 'pass1234'
    course = 'databases'
    assignment = 'assignment1'

    grading_system.login(username, password)

    submission = 'Meh'
    submission_date = '02/20/21'

    grading_system.usr.submit_assignment(course, assignment, submission, submission_date)
    grading_system.reload_data()
    assert grading_system.usr.users[username]['courses'][course][assignment]['submission'] == submission
    assert grading_system.usr.users[username]['courses'][course][assignment]['submission_date'] == submission_date


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem