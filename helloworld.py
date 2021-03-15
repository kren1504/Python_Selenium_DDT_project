import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    #prepara el entorno de la prueba
    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
        driver=cls.driver
        driver.implicitly_wait(10)

    #casos de pruebas y series de acciones
    def test_hello_world(self):
        driver = self.driver
        driver.get('https://www.platzi.com')

    def test_visit_wikipedia(self):
        driver=self.driver
        driver.get('https://wikipedia.org')

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__=="__main__":
    unittest.main(verbosity=2,testRunner=HTMLTestRunner(output='reportes', report_name='hello_world_report' ))

    