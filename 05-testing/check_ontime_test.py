import pytest
import System

#Tests if the program can identify ontime assignments
def test_ontime_assignment(grading_system):
    grading_system.login('hdjsr7', 'pass1234')

    due_date = grading_system.usr.all_courses['cloud_computing']['assignments']['assignment1']['due_date']
    submission_date = grading_system.usr.users['hdjsr7']['courses']['cloud_computing']['assignment1']['submission_date']

    check_ontime = grading_system.usr.users['hdjsr7']['courses']['cloud_computing']['assignment1']['ontime']

    assert check_ontime == grading_system.usr.check_ontime(submission_date, due_date)

    due_date = grading_system.usr.all_courses['databases']['assignments']['assignment2']['due_date']
    submission_date = grading_system.usr.users['hdjsr7']['courses']['databases']['assignment2']['submission_date']

    check_ontime = grading_system.usr.users['hdjsr7']['courses']['databases']['assignment2']['ontime']

    assert check_ontime == grading_system.usr.check_ontime(submission_date, due_date)


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem