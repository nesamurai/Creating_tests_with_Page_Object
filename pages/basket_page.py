from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):

	def should_be_empty_basket_text(self):
		basket_content = self.browser.find_element(*BasketPageLocators.BASKET_MSG)
		content_text = basket_content.text
		print(content_text[:21])
		assert content_text[:21] == "Your basket is empty.", "You have items in the basket, but should not have"

	def should_be_no_items_in_basket(self):
		assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "You have items in the basket, but should not have"