import pytest
from playwright.sync_api import Page
from models.pages.products import ProductsPage
from constants import Constants
from fixtures.products_fixtures import products_page

pytestmark = pytest.mark.products


def test_verify_if_products_title_displayed(page: Page, products_page: ProductsPage, visit_products_page) -> None:
    products_page.verify_products_title()


@pytest.mark.parametrize('product_name', Constants.Products.products_to_add_to_cart)
def test_add_selected_product_to_cart(page: Page, products_page: ProductsPage, product_name: str,
                                      visit_products_page) -> None:
    products_page.add_selected_product_to_cart(product_name, page)


def test_add_random_product_to_cart(page: Page, products_page: ProductsPage, random_product: str,
                                    visit_products_page) -> None:
    products_page.add_selected_product_to_cart(random_product, page)
