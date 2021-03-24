import unittest
from selenium import webdriver
from time import sleep


class MLPrueba(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.get('https://www.mercadolibre.com/')
		driver.find_element_by_id('CO').click()


	def test_browse_navigation(self):
		driver=self.driver
		search_field = driver.find_element_by_xpath('/html/body/header/div/form/input')
		search_field.clear()
		search_field.send_keys('playstation 4')
		search_field.submit()
		sleep(3)
		ubicacion = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section/dl[16]/dd[1]/a/span[1]')
		driver.execute_script("arguments[0].click();", ubicacion)
		sleep(3)
		condicion = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/aside/section[2]/dl[14]/dd[1]/a/span[1]')
		driver.execute_script("arguments[0].click();", condicion)
		orderBy = driver.find_element_by_xpath('//*[@id="root-app"]/div/div/section/div[1]/div/div/div[2]/div[1]/div/div/button')
		driver.execute_script("arguments[0].click();", orderBy)
		sleep(3)
		higherPrice = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div.ui-search-view-options__group > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
		driver.execute_script("arguments[0].click();", higherPrice)
		sleep(3)

		
		titles = []
		prices = []

		for i in range(5):
			title= driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2').text
			price=driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/span[1]/span[2]').text
			titles.append(title)
			prices.append(price)
			
		print("elementos", titles, prices)

		title_and_prices= [ [] for i in range(5)]

		for j in range(5):
			title_and_prices[j].append(titles[j])
			title_and_prices[j].append(prices[j])

	
		print(title_and_prices)

	

	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)