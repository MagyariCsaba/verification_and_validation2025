import datetime
import pytest
from unittest.mock import patch
from employee import Employee
from relations_manager import RelationsManager
from employee_manager import EmployeeManager


@pytest.fixture
def relations_manager():
    return RelationsManager()


@pytest.fixture
def employee_manager(relations_manager):
    return EmployeeManager(relations_manager)


def test_salary_non_leader(employee_manager):
    """Check an employee’s salary who is not a team leader, hired on 10.10.1998, with base salary 1000$."""
    employee = Employee(id=99, first_name="Test", last_name="Employee", base_salary=1000,
                        birth_date=datetime.date(1980, 1, 1), hire_date=datetime.date(1998, 10, 10))
    expected_salary = 1000 + (2025 - 1998) * 100  # 3700
    assert employee_manager.calculate_salary(employee) == expected_salary


def test_salary_team_leader(employee_manager, relations_manager):
    """Check an employee’s salary who is a team leader with 3 team members, hired on 10.10.2008, base salary 2000$."""
    leader = Employee(id=100, first_name="Leader", last_name="Example", base_salary=2000,
                      birth_date=datetime.date(1975, 6, 15), hire_date=datetime.date(2008, 10, 10))
    
    team_members = [
        Employee(id=101, first_name="Member1", last_name="Example", base_salary=1500,
                 birth_date=datetime.date(1990, 1, 1), hire_date=datetime.date(2015, 1, 1)),
        Employee(id=102, first_name="Member2", last_name="Example", base_salary=1600,
                 birth_date=datetime.date(1992, 2, 2), hire_date=datetime.date(2016, 2, 2)),
        Employee(id=103, first_name="Member3", last_name="Example", base_salary=1700,
                 birth_date=datetime.date(1993, 3, 3), hire_date=datetime.date(2017, 3, 3))
    ]

    relations_manager.teams[100] = [101, 102, 103]  # Hozzárendeljük a team tagokat
    relations_manager.employee_list.append(leader)  # Hozzáadjuk a vezetőt az employee listához
    relations_manager.employee_list.extend(team_members)  # Hozzáadjuk a csapattagokat is

    expected_salary = 2000 + (2025 - 2008) * 100 + 3 * 200  # 4300$
    assert employee_manager.calculate_salary(leader) == expected_salary


def test_salary_email_notification(employee_manager):
    """Ensure salary calculation sends correct notification."""
    employee = Employee(id=101, first_name="Notify", last_name="Test", base_salary=2500,
                        birth_date=datetime.date(1985, 5, 20), hire_date=datetime.date(2010, 6, 15))
    
    expected_salary = 2500 + (2025 - 2010) * 100  # 4000
    with patch("builtins.print") as mock_print:
        employee_manager.calculate_salary_and_send_email(employee)
        mock_print.assert_called_with("Notify Test your salary: 4000 has been transferred to you.")
