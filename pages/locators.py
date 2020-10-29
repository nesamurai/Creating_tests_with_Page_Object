from selenium.webdriver.common.by import By

class MainPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
	LOGIN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
	LOGIN_PWD = (By.CSS_SELECTOR, "#id_login-password")
	LOGIN_BTN = (By.NAME, "login_submit")
	REG_EMAIL = (By.CSS_SELECTOR, "#id_registration_email")
	REG_PWD = (By.CSS_SELECTOR, "id_registration_password1")
	REG_CONFIRM = (By.CSS_SELECTOR, "id_registration_password2")
	REG_BTN = (By.NAME, "registration_submit")

class ProductPageLocators():
	ADD_BTN = (By.CLASS_NAME, "btn-add-to-basket")
	BASKET_TOTAL = (By.CLASS_NAME, "basket-mini")
	ITEM_PRICE = (By.CSS_SELECTOR, "div.product_main p.price_color")
	BOOK = (By.TAG_NAME, "h1")
	MSG_ITEM = (By.CSS_SELECTOR, "div.alertinner > strong")