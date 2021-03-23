import csv, unittest
from ddt import ddt, data, unpack
from selenium import webdriver

def get_data(file_name):
	rows = []
	data_file = open(file_name,'r')
	reader = csv.reader(data_file)
	next(reader, None) #omitir la cabecera

	for row in reader:
		rows.append(row)
	return rows


@ddt
class SearchDDT(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\Users\kren1\Documents\curso\Python_con_Selenium\chromedriver.exe')
		driver =self.driver
		driver.get('http://demo-store.seleniumacademy.com/')

	# @data(('dress', 6), ('music',5))
	@data(*get_data('testdata.csv'))
	@unpack

	def test_search_ddt(self,search_value, expected_count):
		driver = self.driver
		serach_field = driver.find_element_by_name("q")
		serach_field.clear()
		serach_field.send_keys(search_value)
		serach_field.submit()

		products = driver.find_elements_by_xpath('//h2[@class="product-name"]/a')
		# print('found', products)
		# for producto in products:
		# 	print(producto.text)

		# self.assertEquals(expected_count, len(products))
		print("lista productors", len(products))
		expected_count = int(expected_count)

		if expected_count > 0:
			self.assertEqual(expected_count, len(products))
		else:
			message = driver.find_element_by_class_name("note-msg")
			self.assertEqual('Your search returns no results.',message.text)

		print('Found ', len(products), 'of products')
		

	def tearDown(self):
		self.driver.close()

if __name__ =="__main__":
	unittest.main(verbosity=2)