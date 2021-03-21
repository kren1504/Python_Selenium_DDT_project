import unittest
from selenium import webdriver
from time import sleep

class NavigationTest(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element_by_link_text('Add/Remove Elements').click()


	def test_browse_navigation(self):
		driver=self.driver

		elements_added = int(input('How many elements will you add'))
		elements_removed = int(input('how many elements will you removed'))
		total_elements = elements_added - elements_removed

		add_button = driver.find_element_by_xpath('//*[@id="content"]/div/button')

		sleep(2)

		for i in range(elements_added):
			add_button.click()
		
		for i in range(elements_removed):
			try:
				# delete_button = driver.find_element_by_xpath('//*[@id="elements"]/button[1]')
				delete_button = driver.find_element_by_class_name('added-manually')
				delete_button.click()
			except:
				print("you are tryying to erase more elements than existe")
				break
		if total_elements > 0:
			print('hay ', total_elements,'en pantalla')
		else:
			print('There are 0 elements on the screen')

		sleep(2)


	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)