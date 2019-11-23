from selenium import webdriver
from getpass import getpass

class Account(object):
	def __init__(self, email , pwd):
		self._email = email
		self._pwd = pwd

	def get_email(self):
		return self._email

	def set_email(self, email):
		self._email = email

	def get_password(self):
		return self._pwd

	def set_password(self, pwd):
		self._pwd = pwd

class FBLogin(object):
	def __init__(self, driver, account):
		self._driver = driver
		self._account = account

	def _access_fb(self):
		self._driver.get("https://facebook.com")

	def _insert_email(self):
		tbEmail = self._driver.find_element_by_css_selector("[name='email']")
		tbEmail.send_keys(self._account.get_email())

	def _insert_password(self):
		tbPwd = self._driver.find_element_by_css_selector("[name='pass']")
		tbPwd.send_keys(self._account.get_password())

	def _submit(self):
		try:
			self._driver.find_element_by_id('loginbutton').click()
		except:
			self._driver.find_element_by_css_selector("[name='login']").click()

	def login(self):
		self._access_fb()
		self._insert_email()
		self._insert_password()
		self._submit()

	def is_success(self):
		return (len(self._driver.find_elements_by_css_selector("[name='pass']")) == 0)



def login_to_facebook(driver):
	print('LOGIN TO FACEBOOK!')
	login = FBLogin(driver, get_account())
	login.login()

	return login.is_success()

def get_account():
	email = str(input("Email> "))
	pwd = getpass("Password for [%s]" %(email))

	return Account(email, pwd)



