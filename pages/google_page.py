from setup.selenium_wrappers import SeleniumDriver
from selenium.webdriver.common.keys import Keys


class GooglePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    search_field_id = 'lst-ib'

    # Variables
    search_term = 'Szukaj w google'

    def search_google(self):
        self.send_keys(self.search_term, self.search_field_id, locator_type='id')
        self.get_element(self.search_field_id, locator_type='id').send_keys(Keys.RETURN)
