import pytest
import random
from test_selectors.products_selectors import ProductsSelectors
from models.pages.products import ProductsPage


@pytest.fixture
def products_page(page):
    return ProductsPage(page)


@pytest.fixture
def visit_products_page(page, base_url):
    page.goto(f'{base_url}/inventory.html')
    yield page


@pytest.fixture()
def random_product(page, base_url, visit_products_page):
    product_names = page.get_by_test_id(ProductsSelectors.product_name).all_text_contents()
    product = random.choice(product_names)
    print(f"🎲 Random product selected: {product}")
    return product
