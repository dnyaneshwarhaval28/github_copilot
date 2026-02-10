import pytest
import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage
from pages.pim_page import PimPage, AddEmployeePage, PimEmployeeListPage
from utils.test_data import generate_employee_name


class TestPimAddEmployee:
    """Test cases for adding employees in OrangeHRM PIM"""

    def test_add_employee_success(self, page, base_url, urls):
        """
        Test Case: Successfully add a new employee
        Scenario: Login -> Navigate to PIM -> Add Employee -> Validate creation
        """
        # Arrange
        first_name, last_name = generate_employee_name("John", "Doe")
        
        # Act - Navigate to login page
        page.goto(base_url)
        
        # Act - Login
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        # Act - Navigate to PIM
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        # Act - Add employee
        pim_page = PimPage(page)
        pim_page.add_employee(first_name, last_name)
        time.sleep(2)
        
        # Assert - Verify employee was added
        assert pim_page.is_employee_present(), \
            "Employee record not found after adding new employee"

    def test_add_employee_with_empty_first_name(self, page, base_url):
        """
        Test Case: Validate required field validation for first name
        Scenario: Attempt to add employee with empty first name
        """
        # Arrange
        last_name = "TestEmployee"
        
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        add_emp_page = AddEmployeePage(page)
        add_emp_page.add_employee("", last_name)
        time.sleep(1)
        
        # Assert
        assert add_emp_page.is_validation_error_displayed(), \
            "Validation error not displayed for empty first name"

    def test_add_employee_with_empty_last_name(self, page, base_url):
        """
        Test Case: Validate required field validation for last name
        Scenario: Attempt to add employee with empty last name
        """
        # Arrange
        first_name = "TestEmployee"
        
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        add_emp_page = AddEmployeePage(page)
        add_emp_page.add_employee(first_name, "")
        time.sleep(1)
        
        # Assert
        assert add_emp_page.is_validation_error_displayed(), \
            "Validation error not displayed for empty last name"

    def test_add_employee_with_both_fields_empty(self, page, base_url):
        """
        Test Case: Validate required field validation for both fields
        Scenario: Attempt to add employee with both first and last name empty
        """
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        add_emp_page = AddEmployeePage(page)
        add_emp_page.add_employee("", "")
        time.sleep(1)
        
        # Assert
        assert add_emp_page.is_validation_error_displayed(), \
            "Validation error not displayed when both fields are empty"


class TestPimSearchEmployee:
    """Test cases for searching employees in OrangeHRM PIM"""

    def test_search_employee_by_name(self, page, base_url):
        """
        Test Case: Search employee by name
        Scenario: Login -> Navigate to PIM List -> Search employee by name -> Validate in table
        """
        # Arrange
        search_name = "Admin"
        
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        pim_list = PimEmployeeListPage(page)
        pim_list.search_employee(search_name)
        time.sleep(2)
        
        # Assert
        assert pim_list.is_employee_in_table(search_name), \
            f"Employee '{search_name}' not found in search results"

    def test_search_employee_no_results(self, page, base_url):
        """
        Test Case: Search employee with non-existent name
        Scenario: Search for employee that doesn't exist
        """
        # Arrange
        non_existent_name = "NonExistentEmployee12345XYZ"
        
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        pim_list = PimEmployeeListPage(page)
        pim_list.search_employee(non_existent_name)
        time.sleep(2)
        
        # Assert
        assert pim_list.is_no_records_displayed(), \
            "Expected 'No Records Found' message when searching for non-existent employee"

    def test_search_employee_case_insensitive(self, page, base_url):
        """
        Test Case: Validate case-insensitive search
        Scenario: Search with different case variations
        """
        # Arrange
        search_name = "admin"  # lowercase
        
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        pim_list = PimEmployeeListPage(page)
        pim_list.search_employee(search_name)
        time.sleep(2)
        
        # Assert
        assert pim_list.get_employee_count() > 0, \
            "Case-insensitive search failed to find employee"

    def test_get_all_employee_names(self, page, base_url):
        """
        Test Case: Retrieve all employee names from the list
        Scenario: Navigate to PIM list and get all employee names
        """
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        pim_list = PimEmployeeListPage(page)
        employee_names = pim_list.get_all_employee_names()
        
        # Assert
        assert len(employee_names) > 0, \
            "No employee names found in the employee list"


class TestPimIntegration:
    """Integration test cases for complete PIM workflows"""

    def test_add_and_search_employee_workflow(self, page, base_url, urls):
        """
        Test Case: Complete workflow - Add employee and search
        Scenario: Login -> Add new employee -> Navigate to list -> Search and validate
        """
        # Arrange
        first_name, last_name = generate_employee_name("TestEmp", "Automation")
        full_name = f"{first_name} {last_name}"
        
        # Act - Add employee
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        add_emp_page = AddEmployeePage(page)
        add_emp_page.add_employee(first_name, last_name)
        time.sleep(2)
        
        # Act - Navigate to employee list
        page.goto(base_url + urls["pim_list"])
        time.sleep(2)
        
        # Act - Search for newly added employee
        pim_list = PimEmployeeListPage(page)
        pim_list.search_employee(first_name)
        time.sleep(2)
        
        # Assert
        assert pim_list.is_employee_in_table(first_name), \
            f"Newly added employee '{full_name}' not found in employee list after search"

    def test_employee_list_displays_correct_count(self, page, base_url):
        """
        Test Case: Validate employee list displays correct employee count
        Scenario: Navigate to PIM list and verify employee count
        """
        # Act
        page.goto(base_url)
        
        login_page = LoginPage(page)
        login_page.login("Admin", "admin123")
        
        dashboard_page = DashboardPage(page)
        dashboard_page.go_to_pim()
        
        pim_list = PimEmployeeListPage(page)
        employee_count = pim_list.get_employee_count()
        
        # Assert
        assert employee_count >= 0, \
            "Employee count should be a non-negative number"
        assert employee_count > 0, \
            "At least one employee should be present in the system"
