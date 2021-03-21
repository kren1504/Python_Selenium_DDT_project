import unittest
from selenium import webdriver
from time import sleep

class DynamicElements(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element_by_link_text('Disappearing Elements').click()


	def test_browse_navigation(self):
		driver=self.driver

		options = []
		menu = 5
		tries =1

		while len(options) < 5:
			options.clear()

			for i in range(menu):
				try:
					option_name = driver.find_element_by_xpath(f'//*[@id="content"]/div/ul/li[{i+1}]/a')
					options.append(option_name.text)
					print(options)
				except:
					print('Option number no encontrada')
					tries +=1
					driver.refresh()
		print("finish in ", tries)

	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)