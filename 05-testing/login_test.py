import pytest
import System

#Tests if the program can correctly log a user into the system
def test_login(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)
    assert grading_system.usr.name == username


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem