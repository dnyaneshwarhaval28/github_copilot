When generating OrangeHRM automation code:

1. Follow POM structure:
   - LoginPage
   - DashboardPage
   - PimEmployeeListPage
   - AddEmployeePage

2. Automate following flows:
   - Login
   - Navigate to PIM
   - Add Employee
   - Search Employee
   - Validate employee in table
   - Validate employee in Employee Information section

3. Add validations:
   - Required field validation
   - Successful employee creation
   - Search result validation

4. Use dynamic employee names.
5. Fetch base_url and endpoints from config.yaml.
6. Write Pytest test cases with clear assertions.
7. Keep methods reusable and modular.
