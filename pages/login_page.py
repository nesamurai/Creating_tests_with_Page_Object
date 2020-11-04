from selenium import webdriver
from .base_page import BasePage
from .locators import LoginPageLocators
import time

class LoginPage(BasePage):
	def should_be_login_page(self):
		self.should_be_login_url()
		self.should_be_login_form()
		self.should_be_register_form()

	def should_be_login_url(self):
		assert "login" in self.browser.current_url, "Substring is not presented in current url"

	def should_be_login_form(self):
		assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL) and \
		self.is_element_present(*LoginPageLocators.LOGIN_PWD) and \
		self.is_element_present(*LoginPageLocators.LOGIN_BTN), "Login form is not presented"

	def should_be_register_form(self):
		assert self.is_element_present(*LoginPageLocators.REG_EMAIL) and \
		self.is_element_present(*LoginPageLocators.REG_PWD) and \
		self.is_element_present(*LoginPageLocators.REG_CONFIRM) and \
		self.is_element_present(*LoginPageLocators.REG_BTN), "Register form is not presented"

	def register_new_user(self, email, password):
		email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL)
		email_field.send_keys(email)

		pwd_field = self.browser.find_element(*LoginPageLocators.REG_PWD)
		pwd_field.send_keys(password)

		confirm_field = self.browser.find_element(*LoginPageLocators.REG_CONFIRM)
		confirm_field.send_keys(password)

		register = self.browser.find_element(*LoginPageLocators.REG_BTN)
		register.click()

		time.sleep(2)