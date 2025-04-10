import pytest
from playwright.sync_api import Browser, Playwright
from models.pages.login import LoginPage
from users import USERS
from fixtures.products_fixtures import random_product, visit_products_page, products_page
from fixtures.login_fixtures import login_page


@pytest.fixture(scope='session')
def base_url():
    return 'https://www.saucedemo.com'


@pytest.fixture(scope='session', autouse=True)
def configure_custom_selector(playwright: Playwright):
    playwright.selectors.set_test_id_attribute('data-test')


@pytest.fixture(scope='session', autouse=True)
def store_auth_state(base_url: str, browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    page.goto(f'{base_url}')
    login_page = LoginPage(page)
    login_page.login(USERS.user.username, USERS.user.password)
    context.storage_state(path='.auth/user.json')
    context.close()


@pytest.fixture()
def auth_context(browser: Browser, store_auth_state):
    context = browser.new_context(storage_state='.auth/user.json')
    yield context
    context.close()


@pytest.fixture()
def page(auth_context):
    page = auth_context.new_page()
    yield page
    page.close()
