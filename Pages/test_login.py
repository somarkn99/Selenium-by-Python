import user_data
from locators.login_locator import loginPageLocators
from constants import DriversEngine

class Testlogin(DriversEngine):
    driver = DriversEngine.Chrome

    def test_username(self, driver):
        element = driver.find_element(*loginPageLocators.username)
        element.clear()
        element.send_keys(user_data.name)
        return element

    def test_password(self, driver):
        element = driver.find_element(*loginPageLocators.password)
        element.clear()
        element.send_keys(user_data.password)
        return element