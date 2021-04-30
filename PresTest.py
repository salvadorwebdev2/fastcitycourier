from selenium import webdriver
import unittest 
from selenium.webdriver.common.keys import Keys
import time

class PageTest(unittest.TestCase):
	def setUp(self):
		self.browser = webdriver.Firefox()
	def test_browser_title(self):
		self.browser.get('http://localhost:9900/')
		self.assertIn('BusinessRegistration',self.browser.title)
	def check_for_rows_in_listtable(self,row_text):
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])
	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:9900/')
		self.assertIn('BusinessRegistration',self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('BusinessRegistration', headerText)
		permit = self.browser.find_element_by_id('permit')
		self.assertEqual(permit.get_attribute('placeholder'), 'Name')
		permit.click()
		time.sleep(1)
		permit.send_keys('Park Jimin')
		time.sleep(1)
		number = self.browser.find_element_by_id('pin')
		self.assertEqual(number.get_attribute('placeholder'),'Number')
		number.click()
		time.sleep(1)
		number.send_keys('123456')
		time.sleep(1)
		address = self.browser.find_element_by_id('blk')
		self.assertEqual(address.get_attribute('placeholder'), 'Address')
		address.click()
		time.sleep(1)
		address.send_keys('Bighit Entertainment South Korea')
		time.sleep(1)		
		business = self.browser.find_element_by_id('bn')
		self.assertEqual(business.get_attribute('placeholder'), 'Business')
		business.click()
		time.sleep(1)
		business.send_keys('Laundry Business')
		time.sleep(1)
		registry = self.browser.find_element_by_id('rn')
		self.assertEqual(registry.get_attribute('placeholder'), 'Registry')
		registry.click()
		time.sleep(1)
		registry.send_keys('000-000')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		address = self.browser.find_element_by_id('blk')
		self.assertEqual(address.get_attribute('placeholder'), 'Address')
		address.click()
		address.send_keys('Philippines')
		time.sleep(1)		
		business = self.browser.find_element_by_id('bn')
		self.assertEqual(business.get_attribute('placeholder'), 'Business')
		business.click()
		time.sleep(1)
		business.send_keys('BTS Accessories')
		time.sleep(1)	
		registry = self.browser.find_element_by_id('rn')
		self.assertEqual(registry.get_attribute('placeholder'), 'Registry')
		registry.click()
		time.sleep(1)
		registry.send_keys('111-111')
		time.sleep(1)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()
		self.check_for_rows_in_listtable('1: Bighit Entertainment South Korea Laundry Business with registry number 000-000')
		self.check_for_rows_in_listtable("1: Philippines BTS Accessories with registry number 111-111")
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_element_by_tag_name('tr')
		#self.assertIn('1: Bighit Entertainment South Korea Laundry Business')
		#self.assertIn('1: Philippines BTS Accessories')
		

		
		
if __name__=='__main__':
	unittest.main()

#browser = webdriver.Firefox()
#browser.get('http://127.0.0.1:9900')
