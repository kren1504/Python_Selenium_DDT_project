import unittest
from selenium import webdriver
from google_page import GooglePage

class GoogleTest(unittest.TestCase):

	@classmethod # para que corran en una sola instancia del navegador
	def setUp(cls):
		cls.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')

	def test_search(self):
		google = GooglePage(self.driver)
		google.open()
		google.search('Platzi')

		self.assertEqual('Platzi', google.keyword)

	@classmethod
	def tearDownClass(cls):
		cls.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)