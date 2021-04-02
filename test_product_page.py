from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest
import random
import string

LOGIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
PRODUCT_PAGE_LINK_SIMPLE = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
PRODUCT_PAGE_LINK_PROMO = \
    "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_PAGE_LINK)
        login_page.open()
        letters = string.ascii_lowercase
        email = ''.join(random.choice(letters) for _ in range(7)) + "@fakemail.org"
        password = ''.join(random.choice(letters) for _ in range(10))
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.product_name_in_add_message_is_correct()
        page.product_price_in_basket_is_correct()


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.product_name_in_add_message_is_correct()
    page.product_price_in_basket_is_correct()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_SIMPLE)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_SIMPLE)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, PRODUCT_PAGE_LINK_PROMO)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_product_in_basket()
    basket_page.should_be_text_about_basket_emptiness()
