from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import WebDriverException

MAX_WAIT = 3
class PageTest(LiveServerTestCase):



	def wait_for_table(self, row_text):        
           start_time = time.time()
           while True:  
               try:                
                   table = self.browser.find_element_by_id('id_table')                  
                   rows = table.find_elements_by_tag_name('tr')                
                   self.assertIn(row_text, [row.text for row in rows])
                   return
               except (AssertionError, WebDriverException) as e:  
                   if time.time() - start_time > MAX_WAIT:  
      	               raise e                  
                   time.sleep(0.5)  
                 
	def setUp(self):
	 self.browser = webdriver.Firefox()

	def test_browser_title(self):
	 self.browser.get('http://localhost:8000/')
	 #self.browser.get(self.live_server_url)
	 self.assertIn('Business Registration',self.browser.title)
	 header_text = self.browser.find_element_by_tag_name('h5').text
	 self.assertIn('Registration', header_text)
	 
	 
	 
	
	 input1 = self.browser.find_element_by_id('on')
	 self.assertEqual(input1.get_attribute('placeholder'),'Enter your fullname')
	 input1.click()
	 time.sleep(1)
	 input1.send_keys('Park Jimin')
	 
	 time.sleep(1)
	 
	 
	 input2 = self.browser.find_element_by_id('od')
	 self.assertEqual(input2.get_attribute('placeholder'),'Enter your ID num')
	 input2.click()
	 time.sleep(1)
	 input2.send_keys('123456')
	 time.sleep(1)
	 
	 
	 btnConfirm = self.browser.find_element_by_id('btnConfirm')
	 btnConfirm.click()
	 time.sleep(2)
	 


	

