import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class NavigationTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.implicitly_wait(10)
		driver.maximize_window()
		driver.get('http://demo-store.seleniumacademy.com/')

	def test_browse_navigation(self):
		WebDriverWait(self.driver, 10).until(lambda s: s.find_element_by_id('select-language').get_attribute('length') == '3')
		account =WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.LINK_TEXT,'ACCOUNT')))
		account.click()

	def test_create_new_customer(self):
		self.driver.find_element_by_link_text('ACCOUNT').click()
		my_account = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "My Account")))
		my_account.click()

		create_account_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT,'CREATE AN ACCOUNT')))
		create_account_button.click()

		WebDriverWait(self.driver, 10).until(EC.title_contains('Create New Customer Account'))



	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)