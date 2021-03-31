from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_NOT_EMPTY), \
            "Product is in basket, but should not be"

    def should_be_text_about_basket_emptiness(self):
        assert not self.is_not_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "There is no text that basket is empty"
