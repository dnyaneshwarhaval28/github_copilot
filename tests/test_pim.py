import pytest
from pages import login_page
from pages import dashboard_page
from pages import pim_page

def test_add_employee(page, base_url):
    print("Base URL:", base_url)
    page.goto(base_url)

    login = login_page.LoginPage(page)
    login.login("Admin", "admin123")

    dashboard = dashboard_page.DashboardPage(page)
    dashboard.go_to_pim()

    pim = pim_page.PimPage(page)
    pim.add_employee("John", "Wick")

def test_search_employee(page):
    page.goto("https://opensource-demo.orangehrmlive.com/")

    login = login_page.LoginPage(page)
    login.login("Admin", "admin123")

    dashboard = dashboard_page.DashboardPage(page)
    dashboard.go_to_pim()

    pim = pim_page.PimPage(page)
    pim.search_employee("John")

    assert pim.is_employee_present(), "Employee not found!"


# def test_add_employee_success(page):
#     page.goto(BASE_URL)

#     # Login
#     login = LoginPage(page)
#     login.login("Admin", "admin123")

#     # Navigate to PIM
#     dashboard = DashboardPage(page)
#     dashboard.go_to_pim()

#     # Add Employee
#     first_name = random_name("John")
#     last_name = random_name("Test")

#     add_emp = AddEmployeePage(page)
#     add_emp.add_employee(first_name, last_name)

#     # Navigate back to Employee List
#     page.goto(BASE_URL + "web/index.php/pim/viewEmployeeList")

#     # Search Employee
#     pim_list = PimEmployeeListPage(page)
#     pim_list.search_employee(first_name)

#     # Validate in table
#     assert pim_list.is_employee_in_table(first_name), "Employee not found in table!"


# def test_add_employee_validation(page):
#     page.goto(BASE_URL)

#     login = LoginPage(page)
#     login.login("Admin", "admin123")

#     dashboard = DashboardPage(page)
#     dashboard.go_to_pim()

#     add_emp = AddEmployeePage(page)
#     add_emp.add_employee("", "")   # empty values

#     assert add_emp.is_validation_error_displayed(), "Validation error not displayed!"

