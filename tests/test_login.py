import pytest
from playwright.sync_api import Page
from models.pages.login import LoginPage
from models.pages.products import ProductsPage
from users import USERS
from fixtures.login_fixtures import login_page


@pytest.mark.login
def test_verify_if_user_logged_in_successfully(base_url: str, page: Page, login_page: LoginPage,
                                               products_page: ProductsPage) -> None:
    page.goto(f'{base_url}')
    login_page.verify_title()
    login_page.verify_if_inputs_are_visible()
    login_page.login(USERS.user.username, USERS.user.password)
    products_page.verify_products_title()
