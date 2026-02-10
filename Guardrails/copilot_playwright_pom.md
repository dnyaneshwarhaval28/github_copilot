When generating Playwright automation code:

- Create separate Page classes for each page.
- Each Page class must inherit from BasePage.
- Store locators as class variables.
- Implement actions as methods in Page classes.
- Do not use page.locator directly in test files.
- Use Pytest fixtures for page and config.
- Use YAML-based config for URLs and browser settings.
- Follow naming convention:
  - Page classes: PascalCase (e.g., PimPage)
  - Methods: snake_case (e.g., add_employee)
  - Test files: test_*.py
