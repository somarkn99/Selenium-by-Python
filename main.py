import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config import Config


class Setup(unittest.TestCase):

    def shortDescription(self,test_case_desc):
        return f"This is for {test_case_desc}"

    # Set up the test environment before each test case
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(Config.BASE_URL)
        self.driver.maximize_window()

    # Clean up the test environment after each test case
    def tearDown(self):
        if self.driver:
            # Quit the WebDriver, closing the browser window
            self.driver.quit()


class TestModule(Setup):
    # to skip this test
    @unittest.skip("Need to be updated after Spring 17")
    # Unit test framework recognize the test cases by the name, should start with test_
    def test_unittest(self):
        short_description = self.shortDescription("Test the Case #TC001")
        print('shortDescription: ',short_description)
        # Here the test code
        try:
            # Wait for an element to be present on the page
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(By.ID, ''))
        finally:
            print("")
            expected_result = ""
            # Get the text of the element
            actual_result = element.text
            # Assert that the expected result matches the actual result
            assert expected_result == actual_result


# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
