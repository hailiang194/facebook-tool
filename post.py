from selenium import webdriver
from time import sleep


class FBPost(object):
	def __init__(self, postElement):
		#init post's content
		try:
			self._content = postElement.find_element_by_css_selector('p').text
		except:
			self._content = ""

		#init link media in this post
		try:
			self._mediaLinks =  postElement.find_element_by_class_name('mtm')
			self._mediaLinks = self._mediaLinks.find_elements_by_css_selector('a')
		except:
			self._mediaLinks = None

		self._react = FBReact(postElement)

	def get_content(self):
		return self._content

	def get_media_links(self):
		if(self._mediaLinks is None):
			return []

		return [media.get_attribute('href') for media in self._mediaLinks]

	def get_react(self):
		return self._react


class FBReact(object):
	def __init__(self, postElement):
		self._reactElement = postElement.find_element_by_css_selector("._6a-y._3l2t._18vj")

	def get_state(self):
		reactText =  self._reactElement.text

		if(reactText != 'Like'):
			return reactText

		if(self._reactElement.value_of_css_property('color') == 'rgb(96, 103, 112)'):
			return 'Nothing'
		else:
			return 'Like'

	def __has_reacted(self):
		return (self.get_state() != 'Nothing')

	def __remove_react(self, driver):
		if(not self.__has_reacted()):
			return

		driver.execute_script("arguments[0].click();", self._reactElement)
		sleep(1)

	def like(self, driver):
		if(self.get_state() == 'Like'):
			return

		self.__remove_react(driver)
		driver.execute_script("arguments[0].click();", self._reactElement)
		sleep(1)


