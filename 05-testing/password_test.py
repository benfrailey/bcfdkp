import pytest
import System

#Tests if the program can handle a wrong password
def test_password(grading_system):
    username = 'akend3'
    password =  '123454321'
    grading_system.login(username,password)
    assert grading_system.usr.password == password


@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem