import pytest
from playwright.sync_api import Browser, Page, Playwright
from models.pages.login import LoginPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    return LoginPage(page)
