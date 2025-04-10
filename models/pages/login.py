from playwright.sync_api import expect
from test_selectors.login_selectors import LoginSelectors
from constants import Constants


class LoginPage:
    def __init__(self, page):
        self.page = page
        self.app_title = page.get_by_text(Constants.Titles.app)
        self.email_input = page.get_by_test_id(LoginSelectors.email_input)
        self.password_input = page.get_by_test_id(LoginSelectors.password_input)
        self.login_button = page.locator(LoginSelectors.login_button)

    def verify_title(self):
        expect(self.app_title).to_be_visible()

    def verify_if_inputs_are_visible(self):
        expect(self.email_input).to_be_visible()
        expect(self.password_input).to_be_visible()

    def fill_email(self, email):
        self.email_input.fill(email)

    def fill_password(self, password):
        self.password_input.fill(password)

    def click_login_button(self):
        expect(self.login_button).to_be_visible()
        self.login_button.click()

    def login(self, email, password):
        self.fill_email(email)
        self.fill_password(password)
        self.click_login_button()
