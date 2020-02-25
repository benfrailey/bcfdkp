import pytest
import System

#Tests if the program will fail if an incorrect password is entered
def test_bad_password(grading_system):
    username = 'akend3'
    password =  'badPass'
    grading_system.login(username,password)
    assert grading_system.usr.password != password


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem