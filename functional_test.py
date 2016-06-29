# webdriver is a tool for automating web application testing and in particular to verify that they work as expected/
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    """
    setUp and tearDown methods allow to define instructions that will be
    executed before and after each test method.
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # to checkout its homepage
        self.browser.get('http://localhost:8000')

        # notice that the page title and header mention 'to-do lists'
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # typing 'Buy peacock feathers' into a text box
        inputbox.send_keys('Buy peacock feathers')
        # when hitting the enter key, the page updates, and now the page lists has an to-do item in to-do list table
        inputbox.send_keys(Keys.ENTER)

        # find_element_by， return one element, or rases an exception if it can't find it
        # find_elements_by, return one list, can be an empty list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # be able to enter another to-do item


        # Stop the test run on the first error or failure.
        self.fail('Finish the test!')

# unittest.main() provides a command-line interface to the test script.
if __name__ == '__main__':

    # this launches the unittest test runner which will automatically find test classes and methods in the file and run them.
    unittest.main(warnings='ignore')
