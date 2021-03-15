import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class AssertionsTest(unittest.TestCase):

    #prepara el entorno de la prueba
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
        driver=self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        
    def test_search_field(self):
        self.assertTrue(self.if_element_present(By.NAME,'q'))

    def test_languaje_option(self):
        self.assertTrue(self.if_element_present(By.ID, 'select-languaje'))
    

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchException as variable:
            return False
        return True
        

if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))