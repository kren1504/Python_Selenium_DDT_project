from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class MLPages(object):
	def __init__(self,driver):
		self._driver = driver
		self._url = 'https://www.mercadolibre.com/'

	def set(self,web):
		self._driver = web

	@property
	def is_located(self):
			WebDriverWait(self._driver, 10).until(EC.presence_of_all_elements_located((By.NAME, 'q')))
			return True

	@property
	def keyword(self):
		input_field =  self._driver.find_element_by_name('q')
		return input_field.get_attribute('value')

	def open(self):
		self._driver.get(self._url)
		botton_colombia = self._driver.find_element_by_id('CO')
		web_colombia =  botton_colombia.click_submit()
		self._driver.set(self,web_colombia)

	def type_search(self,keyword):
		input_field =  self._driver.find_element_by_name('q')
		input_field.send_keys(keyword)

	def click_submit(self):
		input_field =  self._driver.find_element_by_name('')
		input_field.submit()

	def search(self, keyword):
		self.type_search(keyword)
		self.click_submit()

