from .base_page import BasePage
from selenium.webdriver.common.by import By
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