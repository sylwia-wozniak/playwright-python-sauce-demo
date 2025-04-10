### Overview
The Playwright UI Automation for end-to-end UI testing using Playwright and pytest.

### Features
#### Page Object Model (POM)
Implements the Page Object Model pattern to encapsulate web elements and actions within separate page classes, improving test maintainability and readability.
#### Login session
Manages login functionality using session storage to persist authentication state across multiple tests, enabling seamless login during test execution.
#### Fixtures
Utilizes pytest fixtures for setup, ensuring reusable and isolated test environments, including context and page initialization.

### Installation
1. Clone the repository<br>
2. Create and activate a virtual environment<br>
`python -m venv venv`<br>
`source venv/bin/activate  # On Windows: venv\Scripts\activate`<br>
3. ️Install dependencies<br>
`pip install -r requirements.txt`<br>
`playwright install`<br>

### Running Tests
#### Run All Tests
`pytest`
#### Run Login Tests Only
`pytest -m login`
#### Run Products Tests Only
`pytest -m products`
