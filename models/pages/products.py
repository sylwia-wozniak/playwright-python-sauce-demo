from playwright.sync_api import expect, Page
from constants import Constants
from test_selectors.products_selectors import ProductsSelectors


class ProductsPage:
    def __init__(self, page):
        self.page = page
        self.products_title = page.get_by_text(Constants.Titles.products)
        self.products_name = page.get_by_test_id(ProductsSelectors.product_name)
        self.add_to_cart_button = page.get_by_text(Constants.Buttons.add_to_cart_button)
        self.products_description = page.get_by_test_id(ProductsSelectors.products_description)

    def verify_products_title(self):
        expect(self.products_title).to_be_visible()

    def add_selected_product_to_cart(self, product_name: str, page: Page):
        product_summary = self.products_description.locator('div', has=page.get_by_test_id(
            ProductsSelectors.product_name)).filter(has_text=product_name).locator('..')
        add_to_cart_button = product_summary.locator(self.add_to_cart_button)
        add_to_cart_button.click()
