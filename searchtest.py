import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class SearchTests(unittest.TestCase):

    #prepara el entorno de la prueba
    
    def setUp(self):
        self.driver=webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
        driver=self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.get('http://demo-store.seleniumacademy.com/')
        
    def tests_search_tee(self):
        driver=self.driver
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        search_field.send_keys('tee')
        search_field.submit()

    def test_search_salt_shaker(self):
        driver=self.driver
        search_field= driver.find_element_by_id('q')

        search_field.send_keys('salt')
        search_field-submit()

        products = driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div[2]/div[2]/div[3]/ul/li/div/h2/a')
        self.assertEqual(1,len(products))

    

    def tearDown(self):
        self.driver.quit()

 
        

if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report'))