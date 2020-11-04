from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

	def add_to_basket(self):
		knopka = self.browser.find_element(*ProductPageLocators.ADD_BTN)
		knopka.click()

	def should_be_item_added(self):
		book = self.browser.find_element(*ProductPageLocators.BOOK)
		title = book.text
		print(title)
		message = self.browser.find_element(*ProductPageLocators.MSG_ITEM)
		msg_text = message.text
		print(msg_text)
		assert title == msg_text, "Selected item was not added to basket"

	def should_be_same_cost(self):
		purchase = self.browser.find_element(*ProductPageLocators.BASKET_TOTAL)
		ptext = purchase.text
		print(ptext[14:20].strip())
		book = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
		price = book.text
		print(price)
		assert ptext[14:20].strip() == price, "Basket total is not equal to book price"

	def should_not_be_success_message(self):
		assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message is presented, but should not be"

	def should_dissapear(self):
		assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
		"Success message dissapeared, but should not"