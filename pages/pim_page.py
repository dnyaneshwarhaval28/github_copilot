from pages.base_page import BasePage

class PimPage(BasePage):

    ADD_EMPLOYEE_BTN = "//button[normalize-space()='Add']"
    FIRST_NAME = "input[name='firstName']"
    LAST_NAME = "input[name='lastName']"
    SAVE_BTN = "//button[normalize-space()='Save']"

    EMP_NAME_SEARCH = "(//input[@placeholder='Type for hints...'])[1]"
    SEARCH_BTN = "//button[normalize-space()='Search']"
    EMP_RECORD = "//div[@class='oxd-table-body']//div[@role='row']"

    def add_employee(self, first_name, last_name):
        self.click(self.ADD_EMPLOYEE_BTN)
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.click(self.SAVE_BTN)

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
        return self.page.locator(self.REQUIRED_ERROR).count() > 0

class PimEmployeeListPage(BasePage):

    EMP_NAME_SEARCH = "(//input[@placeholder='Type for hints...'])[1]"
    SEARCH_BTN = "//button[normalize-space()='Search']"

    TABLE_ROWS = "//div[@class='oxd-table-body']//div[@role='row']"
    TABLE_EMP_NAME = "//div[@class='oxd-table-body']//div[@role='row']//div[3]"

    def search_employee(self, name):
        self.fill(self.EMP_NAME_SEARCH, name)
        self.click(self.SEARCH_BTN)

    def is_employee_in_table(self, name):
        rows = self.page.locator(self.TABLE_EMP_NAME).all_inner_texts()
        return any(name in row for row in rows)
