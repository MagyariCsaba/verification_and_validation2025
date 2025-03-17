import datetime
import pytest
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager

@pytest.fixture
def relations_manager():
    return RelationsManager()

@pytest.fixture
def employee_manager(relations_manager):
    return EmployeeManager(relations_manager)

def test_john_doe_is_team_leader(relations_manager):
    """Check if John Doe is a team leader and has the correct birthdate"""
    john_doe = next(e for e in relations_manager.get_all_employees() if e.first_name == "John" and e.last_name == "Doe")
    assert relations_manager.is_leader(john_doe)
    assert john_doe.birth_date == datetime.date(1970, 1, 31)

def test_john_doe_team_members(relations_manager):
    """Check if John Doe’s team members are Myrta Torkelson and Jettie Lynch"""
    john_doe = next(e for e in relations_manager.get_all_employees() if e.id == 1)
    team_members = relations_manager.get_team_members(john_doe)
    member_names = {(e.first_name, e.last_name) for e in team_members}
    expected_members = {("Myrta", "Torkelson"), ("Jettie", "Lynch")}
    assert member_names == expected_members

def test_tomas_andre_not_in_john_doe_team(relations_manager):
    """Make sure that Tomas Andre is not John Doe’s team member"""
    john_doe = next(e for e in relations_manager.get_all_employees() if e.id == 1)
    team_members = relations_manager.get_team_members(john_doe)
    assert not any(e.first_name == "Tomas" and e.last_name == "Andre" for e in team_members)

def test_gretchen_watford_salary(relations_manager):
    """Check if Gretchen Watford’s base salary equals 4000$"""
    gretchen = next(e for e in relations_manager.get_all_employees() if e.first_name == "Gretchen" and e.last_name == "Watford")
    assert gretchen.base_salary == 4000

def test_tomas_andre_not_a_leader(relations_manager):
    """Make sure Tomas Andre is not a team leader and check behavior when retrieving his team members"""
    tomas = next(e for e in relations_manager.get_all_employees() if e.first_name == "Tomas" and e.last_name == "Andre")
    assert not relations_manager.is_leader(tomas)
    assert relations_manager.get_team_members(tomas) is None

def test_jude_overcash_not_in_db(relations_manager):
    """Make sure that Jude Overcash is not stored in the database"""
    employees = relations_manager.get_all_employees()
    assert not any(e.first_name == "Jude" and e.last_name == "Overcash" for e in employees)
