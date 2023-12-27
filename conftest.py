import pytest

from constants import Drivers


# Scope session:
# Run all test cases within the same window (does not close the browser window)
# Scope function
# Run all test cases each one independently
@pytest.fixture(scope="session")
def browser(self):
    driver = Drivers.Chrome
    yield driver
    driver.quit()