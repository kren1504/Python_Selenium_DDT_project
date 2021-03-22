import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver


class Tables(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.get('http://the-internet.herokuapp.com/')
		driver.find_element_by_link_text('Sortable Data Tables').click()


	def test_sort_table(self):
		driver = self.driver
		table_data = [[] for i in range(5)]
		print(table_data)
		
		for i in range(4):
			header = driver.find_element_by_xpath(f'//*[@id="table2"]/thead/tr/th[{i+1}]/span')
			table_data[i].append(header.text)

			for j in range (4):
				row_data=driver.find_element_by_xpath(f'//*[@id="table2"]/tbody/tr[{i+1}]/td[{j+1}]')
				table_data[i].append(row_data.text)
				print("i", i+1,"j",j+1,"header",header.text,"rd ",row_data.text, )

		print(table_data)



	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)