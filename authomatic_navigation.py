import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.implicitly_wait(10)
		driver.maximize_window()
		driver.get('http://www.google.com/')

	def test_browse_navigation(self):
		driver=self.driver
		search_field=driver.find_element_by_name('q')
		search_field.clear()
		search_field.send_keys('platzi')
		search_field.submit()
		driver.back()
		sleep(2)
		driver.forward()
		sleep(2)
		driver.refresh()
		sleep(2)
		



	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)