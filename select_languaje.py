import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class LanguajeOption(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver = self.driver
		driver.implicitly_wait(30)
		driver.maximize_window()
		driver.get("http://demo-store.seleniumacademy.com/")
	
	def test_select_languaje(self):
        exp_options = ['English', 'French', 'German']
        act_options= []
        select_languaje= Select(self.driver.find_element_by_id('select-languaje'))
        self.assertEqual(3,len(select_languaje))

        for option in select_languaje:
            act_options.append(option.text)
        
        self.assertListEqual(exp_options,act_options)

        self.assertEqual('English',select_languaje.first_selected_option.text)

        select_languaje.select_by_visible_text('German')

        self.assertTrue('store=german' in self.driver.current_url)

        select_languaje =  Select(self.driver.find_element_by_id('select-languaje'))
        select_languaje.select_by_index(0)


	def tearDown(self):
		self.driver.implicitly_wait(3)
		self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)