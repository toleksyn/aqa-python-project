import pytest

from pages.rozetka_cart_modal import RozetkaCartModal
from pages.rozetka_home_page import RozetkaHomePage
from pages.rozetka_product_page import RozetkaProductPage
from pages.rozetka_search_results_page import RozetkaSearchResultsPage


@pytest.fixture
def rozetka_home_page():
    return RozetkaHomePage()

@pytest.fixture
def  rozetka_search_results_page():
    return RozetkaSearchResultsPage()

@pytest.fixture
def  rozetka_product_page():
    return RozetkaProductPage()
    ProductPage()

@pytest.fixture
def rozetka_cart_modal():
    return RozetkaCartModal()