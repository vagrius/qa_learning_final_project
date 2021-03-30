from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_button.click()

    def product_name_in_add_message_is_correct(self):
        pr_name_in_msg = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text
        pr_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert pr_name_in_msg == pr_name, "Product name doesn't match with ones in message"

    def product_price_in_basket_is_correct(self):
        pr_price_in_bsk = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET).text
        pr_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert pr_price_in_bsk == pr_price, "Product price doesn't match with ones in basket"
