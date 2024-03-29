from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		# Edith has heard about a cool new onLine to-do app. She goes
		# to check out its homepage
		self.browser.get('http://localhost:8000')

		# She notices the page title and header mention to-do lists
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# She is invited to enter a todo item straight away
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'),
			'Enter a to-do item'
		)

		#She types "buy peacock features" into a text box 
		inputbox.send_keys('Buy peacock feathers')

		#When she hits enter, the page updates, and now the page lists
		# 1. "Buy peacock feathers" as an item in a to-do list table
		inputbox.send_keys(Keys.ENTER)

		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(
			any(row.text == '1: Buy peacock feathers' for row in rows),
			"New to-do item did not appear in table"
		)

		#Thers is stille a textbox inviting her to add another to-do item
		#She enters "use peacocks feathers to make a fly"
		self.fail('Finish the test!')

if __name__ == '__main__':
	unittest.main()