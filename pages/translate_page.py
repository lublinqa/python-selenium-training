from setup.selenium_wrappers import SeleniumDriver
from selenium.webdriver.common.keys import Keys


class GoogleTranslatePage(SeleniumDriver):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    search_field_name = "text"
    input = "dog"
    result_field_id = "result_box"

    # Variables

    def check_google_translate(self):
        self.send_keys(self.input, self.search_field_name, locator_type="name")
        import time
        time.sleep(5)
        assert self.element_presence(self.result_field_id, locator_type="id")