from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
import pytest


class SeleniumDriver(object):

    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def get_by_type(locator_type):
        locator_type = locator_type.lower()
        if locator_type == 'id':
            return By.ID
        elif locator_type == 'name':
            return By.NAME
        elif locator_type == 'xpath':
            return By.XPATH
        elif locator_type == 'css':
            return By.CSS_SELECTOR
        elif locator_type == 'class':
            return By.CLASS_NAME
        elif locator_type == 'link':
            return By.LINK_TEXT
        else:
            pytest.fail('Locator type ' + locator_type +
                        ' not correct/supported')
        return False

    def get_element(self, locator, locator_type='css'):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((by_type, locator)))
            element = self.driver.find_element(by_type, locator)
        except:
            pytest.fail('Element not found with locator: ' + locator +
                        ' and locatorType: ' + locator_type)
        return element

    def send_keys(self, data, locator, locator_type='css'):
        try:
            element = self.get_element(locator, locator_type)
            element.send_keys(data)
        except:
            pytest.fail('Cannot send data on the element with locator: ' + locator +
                        ' locatorType: ' + locator_type)

    def locator_click(self, locator, locator_type='css'):
        try:
            element = self.get_element(locator, locator_type)
            element.click()
        except:
            pytest.fail('Cannot click on the element with locator: ' + locator +
                        ' locatorType: ' + locator_type)

    def element_presence(self, locator, locator_type='css'):
        try:
            element = self.get_element(locator, locator_type)
            if element is not None:
                return True
            else:
                return False
        except:
            return False
