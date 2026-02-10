from pages.base_page import BasePage

class DashboardPage(BasePage):
    PIM_MENU = "//span[text()='PIM']"

    def go_to_pim(self):
        self.click(self.PIM_MENU)
