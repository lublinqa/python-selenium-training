from setup.selenium_wrappers import SeleniumDriver
from selenium.webdriver.common.keys import Keys


class GooglePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    search_field_id = 'lst-ib'
    currency_box = '.dDoNo'

    # Variables
    search_term = '1 USD to PLN'

    def check_currency_box(self):
        self.element_presence(self.search_field_id, locator_type='id')
        self.send_keys(self.search_term, self.search_field_id, locator_type='id')
        self.get_element(self.search_field_id, locator_type='id').send_keys(Keys.RETURN)
        assert self.element_presence(self.currency_box)
