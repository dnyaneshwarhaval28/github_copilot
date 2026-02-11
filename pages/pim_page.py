from pages.base_page import BasePage

class PimPage(BasePage):

    ADD_EMPLOYEE_BTN = "//button[normalize-space()='Add']"
    FIRST_NAME = "input[name='firstName']"
    LAST_NAME = "input[name='lastName']"
    SAVE_BTN = "//button[normalize-space()='Save']"
    employee_profile = "//div[@class='orangehrm-edit-employee-name']/h6"

    EMP_NAME_SEARCH = "(//input[@placeholder='Type for hints...'])[1]"
    SEARCH_BTN = "//button[normalize-space()='Search']"
    EMP_RECORD = "//div[@class='oxd-table-body']//div[@role='row']"

    def add_employee(self, first_name, last_name):
        self.click(self.ADD_EMPLOYEE_BTN)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.click(self.SAVE_BTN)

    def verify_employee_added(self):
        locator = self.page.locator(self.employee_profile)
        locator.wait_for(state="visible")
        actual_name = locator.inner_text().strip()
        return actual_name

    def search_employee(self, name):
        self.fill(self.EMP_NAME_SEARCH, name)
        self.click(self.SEARCH_BTN)

    def is_employee_present(self):
        return self.page.locator(self.EMP_RECORD).count() > 0
    
class AddEmployeePage(BasePage):

    ADD_BTN = "//button[normalize-space()='Add']"
    FIRST_NAME = "input[name='firstName']"
    LAST_NAME = "input[name='lastName']"
    SAVE_BTN = "//button[normalize-space()='Save']"

    REQUIRED_ERROR = "//span[contains(@class,'oxd-input-field-error-message')]"

    def add_employee(self, first_name, last_name):
        self.click(self.ADD_BTN)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.click(self.SAVE_BTN)

    def is_validation_error_displayed(self):
        try:
            self.page.locator(self.REQUIRED_ERROR).wait_for(timeout=3000)
            return True
        except:
            return False


class PimEmployeeListPage(BasePage):
    """Page Object for PIM Employee List - Search and validate employees"""

    # Search locators
    EMP_NAME_SEARCH = "(//input[@placeholder='Type for hints...'])[1]"
    SEARCH_BTN = "//button[normalize-space()='Search']"
    
    # Table locators
    TABLE_BODY = "//div[@class='oxd-table-body']"
    TABLE_ROWS = "//div[@class='oxd-table-body']//div[@role='row']"
    TABLE_EMP_NAME_CELL = "//div[@class='oxd-table-body']//div[@role='row']//div[2]"
    
    # No records message
    NO_RECORDS_MSG = "//span[contains(text(),'No Records Found')]"

    def search_employee(self, name):
        """
        Search for an employee by name in the search field.
        
        Args:
            name (str): Employee name to search
        """
        self.fill(self.EMP_NAME_SEARCH, name)
        self.click(self.SEARCH_BTN)
        self.wait_for(self.TABLE_BODY)

    def is_employee_in_table(self, name):
        """
        Validate if employee exists in the table by name.
        
        Args:
            name (str): Employee name to validate
            
        Returns:
            bool: True if employee found in table, False otherwise
        """
        try:
            rows = self.page.locator(self.TABLE_EMP_NAME_CELL).all_inner_texts()
            return any(name.lower() in row.lower() for row in rows)
        except Exception:
            return False

    def get_employee_count(self):
        """
        Get total number of employees displayed in the table.
        
        Returns:
            int: Number of employee records in the table
        """
        return self.page.locator(self.TABLE_ROWS).count()

    def is_no_records_displayed(self):
        """
        Check if 'No Records Found' message is displayed.
        
        Returns:
            bool: True if no records message is visible, False otherwise
        """
        return self.is_visible(self.NO_RECORDS_MSG)

    def get_all_employee_names(self):
        """
        Get list of all employee names in the table.
        
        Returns:
            list: List of employee names from the table
        """
        try:
            return self.page.locator(self.TABLE_EMP_NAME_CELL).all_inner_texts()
        except Exception:
            return []
    TABLE_EMP_NAME = "//div[@class='oxd-table-body']//div[@role='row']//div[3]"

    def search_employee(self, name):
        self.fill(self.EMP_NAME_SEARCH, name)
        self.click(self.SEARCH_BTN)

    def is_employee_in_table(self, name):
        rows = self.page.locator(self.TABLE_EMP_NAME).all_inner_texts()
        return any(name in row for row in rows)
