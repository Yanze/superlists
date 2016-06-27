# webdriver is a tool for automating web application testing and in particular to verify that they work as expected/
from selenium import webdriver
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

        # Stop the test run on the first error or failure.
        self.fail('Finish the test!')

# unittest.main() provides a command-line interface to the test script.
if __name__ == '__main__':

    # this launches the unittest test runner which will automatically find test classes and methods in the file and run them.
    unittest.main(warnings='ignore')
