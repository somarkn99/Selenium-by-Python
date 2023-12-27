import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Setup(unittest.TestCase):

    def shortDescription(self,testCaseDesc):
        return "This is for {testCaseDesc}"

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.somar-kesen.com")
        self.driver.maximize_window()

    def tearDown(self):
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
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(By.ID, ''))
        finally:
            print("")
            expected_result = ""
            actual_result = element.text
            assert expected_result == actual_result


if __name__ == '__main__':
    unittest.main()
